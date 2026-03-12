from backend.scraper import get_character_content
from bs4 import BeautifulSoup
import re
import unicodedata


def character_data(param: str):
    source = get_character_content(param)
    if source["status"] != "ok":
        return source

    html = source["html"]
    soup = BeautifulSoup(html, features="html.parser")

    def get_content(soup):
        find_birth = soup.find(string=re.compile(r"nascimento:", re.IGNORECASE))
        if not find_birth:
            return None
        return find_birth.find_parent("div")

    content = get_content(soup)
    if not content:
        return {"status": "not_found", "html": None}

    def get_name(soup):
        name = soup.find("span", string=re.compile("Personagens"))
        if name:
            text = name.get_text(strip=True)
            result = text.replace(" | ", ",").split(",", 1)
            return result[1]
        return None

    def get_profile_image():
        img = content.find("img")
        if img and img.get("src"):
            return img["src"]
        return None

    def get_bio(soup):
        bio_title = soup.find("h4", string=re.compile("Biografia"))
        if not bio_title:
            return ""
        content_bio = []
        for p in bio_title.find_next_siblings():
            if p.name == "p":
                text = p.get_text().replace("\xa0", " ")
                content_bio.append(text)
            else:
                break
        return " ".join(content_bio)

    def normalize_label(label: str) -> str:
        cleaned = label.replace("\xa0", " ").strip().lower()
        without_accents = "".join(
            ch
            for ch in unicodedata.normalize("NFKD", cleaned)
            if not unicodedata.combining(ch)
        )
        return " ".join(without_accents.split())

    label_to_key = {
        "ano de nascimento": "birth",
        "de nascimento": "birth",
        "tipo sanguineo": "bloodType",
        "altura": "height",
        "peso": "weight",
    }

    data = {}
    character_name = get_name(soup)
    character_img = get_profile_image()

    if character_name:
        data["name"] = character_name
    if character_img:
        data["img"] = character_img

    text = content.get_text(separator="\n", strip=True)
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        field = label_to_key.get(normalize_label(key))
        if field:
            data[field] = value.strip()

    data["bio"] = get_bio(soup)

    if not data.get("name"):
        return {"status": "not_found", "html": None}

    return {"status": "ok", "data": data}
