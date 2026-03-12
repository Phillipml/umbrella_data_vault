# %%

from backend.scraper import get_character_content
from bs4 import BeautifulSoup
import re


def character_data(param: str):
    html = get_character_content(param)
    if html == "Error":
        print("Erro na requisição, verificar se o parametro do personagem está correto")
        return None

    soup = BeautifulSoup(html, features="html.parser")

    def get_content(soup):
        find_birth_date = soup.find("em", string=re.compile("nascimento:"))
        if not find_birth_date:
            return None
        return find_birth_date.find_parent("div")

    content = get_content(soup)

    def get_name(soup):
        name = soup.find("span", string=re.compile("Personagens"))
        if name:
            text = name.get_text(strip=True)
            result = text.replace(" | ", ",").split(",", 1)
            return result[1]
        return None

    def get_profile_image():
        if not content:
            return None
        img = content.find("img")
        if img and img.get("src"):
            img_src = img["src"]
            return {"img_src": img_src}
        return None

    def get_bio(soup):
        bio_title = soup.find("h4", string=re.compile("Biografia"))
        if not bio_title:
            return []
        content_bio = []
        for p in bio_title.find_next_siblings():
            if p.name == "p":
                text = p.get_text().replace("\xa0", " ")
                content_bio.append(text)
            else:
                break
        return " ".join(content_bio)

    def get_basic_infos():
        character_data = {}
        if content:
            character_name = get_name(soup)
            character_img = get_profile_image()

            if character_name:
                character_data["name"] = character_name
            if character_img:
                character_data["img"] = character_img["img_src"]
            character_ems = content.find_all("em")

            for i in character_ems:
                text = i.get_text(strip=True)
                LABEL_TO_KEY = {
                    "Name": "name",
                    "Img": "img",
                    "Ano de nascimento": "birth",
                    "Tipo sanguíneo": "bloodType",
                    "Altura": "height",
                    "Peso": "weight",
                    "Bio": "bio",
                }
                if ":" in text:
                    key, value = text.split(":", 1)
                    field = LABEL_TO_KEY.get(key.strip())
                    character_data[field] = value.strip()
        character_bio = get_bio(soup)
        character_data["bio"] = character_bio
        return character_data

    return get_basic_infos()


# %%
