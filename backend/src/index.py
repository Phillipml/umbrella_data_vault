import sys
from pathlib import Path

_src = Path(__file__).resolve().parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from fastapi import FastAPI, HTTPException
from backend.parsers.character_list import get_all_characters
from backend.parsers.character_detail import character_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://umbrella-data-vault-u51w.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Umbrella": "Data System"}


@app.get("/characters-list")
def character_list():
    try:
        result = get_all_characters()
        if result == "Error" or (isinstance(result, str) and "Erro" in result):
            raise HTTPException(
                status_code=503, detail="Source temporarily unavailable"
            )
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=503, detail="Source temporarily unavailable"
        ) from e


@app.get("/character-bio/{param}")
def get_character_bio(param: str):
    try:
        result = character_data(param)
        status = result.get("status")

        if status == "not_found":
            raise HTTPException(
                status_code=404,
                detail="Character not found at source",
            )

        if status != "ok":
            raise HTTPException(
                status_code=503,
                detail="Source temporarily unavailable",
            )

        return result["data"]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail="Source temporarily unavailable",
        ) from e
