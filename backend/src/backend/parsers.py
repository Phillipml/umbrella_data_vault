# %%
from backend.scraper import get_character_content
from bs4 import BeautifulSoup
import re

html = get_character_content("Jill Valentine")
if html == "Error":
    print("Erro na requisição, verificar se o nome do personagem está correto")

soup = BeautifulSoup(html, features="html.parser")


def get_name(soup):
    name = soup.find("span", string=re.compile("Personagens"))
    if name:
        text = name.get_text(strip=True)
        result = text.replace(" | ", ",").split(",", 1)
        return result[1]
    return None


def get_profile_image(soup):
    img = soup.find("img")
    if img and img.get("src"):
        img_src = img["src"]
        return {"img_src": img_src}
    return None


def get_basic_infos(soup):
    character_data = {}

    find_birth_date = soup.find("em", string=re.compile("Ano de nascimento"))

    if find_birth_date:
        character_name = get_name(soup)
        character_img = get_profile_image(soup)

        if character_name:
            character_data["name"] = character_name
        if character_img:
            character_data["img_src"] = character_img["img_src"]
        character_div_content = find_birth_date.find_parent("div")
        character_ems = character_div_content.find_all("em")

        for i in character_ems:
            text = i.get_text(strip=True)

            if ":" in text:
                key, value = text.split(":", 1)
                character_data[key.strip()] = value.strip()

    return character_data


get_basic_infos(soup)
# %%
