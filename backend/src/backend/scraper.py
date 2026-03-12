from .config import cookies, headers
import requests

NOT_FOUND_MARKERS = (
    "ooops... erro 404",
    "a pagina que esta a procura nao existe",
    "a página que está à procura não existe",
)


def _is_not_found_page(html: str) -> bool:
    content = html.lower()
    return any(marker in content for marker in NOT_FOUND_MARKERS)


def get_character_content(param: str):
    try:
        res = requests.get(
            f"https://www.residentevildatabase.com/personagens/{param}/",
            cookies=cookies,
            headers=headers,
            timeout=15,
        )
    except requests.RequestException:
        return {"status": "source_unavailable", "html": None}

    if res.status_code == 404:
        return {"status": "not_found", "html": None}

    if res.status_code != 200:
        return {"status": "source_unavailable", "html": None}

    if _is_not_found_page(res.text):
        return {"status": "not_found", "html": None}

    return {"status": "ok", "html": res.text}


def get_character_list():
    try:
        res = requests.get(
            "https://www.residentevildatabase.com/personagens/",
            cookies=cookies,
            headers=headers,
            timeout=15,
        )
    except requests.RequestException:
        return "Error"

    if res.status_code != 200:
        return "Error"

    return res.text
