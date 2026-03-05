# %%
from config import cookies, headers
import re
import requests


def get_character_content(name: str):
    character = re.sub(r"[(),.]", "", name.strip().lower()).replace(" ", "-")
    res = requests.get(
        f"https://www.residentevildatabase.com/personagens/{character}/",
        cookies=cookies,
        headers=headers,
    )
    if res.status_code != 200:
        return "Error"
    return res.text
