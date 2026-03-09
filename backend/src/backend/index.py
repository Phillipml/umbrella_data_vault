from fastapi import FastAPI
from backend.parsers.character_list import get_all_characters
from backend.parsers.character_detail import character_data

app = FastAPI()


@app.get("/")
def read_root():
    return {"Umbrella": "Data System"}


@app.get("/characters_list")
def character_list():
    return get_all_characters()


@app.get("/character-bio/{param}")
def get_character_bio(param: str):
    return character_data(param)
