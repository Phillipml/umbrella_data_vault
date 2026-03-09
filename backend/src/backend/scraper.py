# %%
from .config import cookies, headers
import re
import requests


def get_character_content(param: str):
    res = requests.get(
        f"https://www.residentevildatabase.com/personagens/{param}/",
        cookies=cookies,
        headers=headers,
    )
    if res.status_code != 200:
        return "Error"
    return res.text


def get_character_list():
    res = requests.get(
        f"https://www.residentevildatabase.com/personagens/",
        cookies=cookies,
        headers=headers,
    )
    if res.status_code != 200:
        return "Error"
    return res.text
