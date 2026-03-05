# %%
from backend.scraper import get_character_content
from bs4 import BeautifulSoup
import re

html = get_character_content("Jill Valentine")
if html == "Error":
    print("Erro na requisição, verificar se o nome do personagem está correto")

soup = BeautifulSoup(html, features="html.parser")

find_birth_date = soup.find("em", string=re.compile("Ano de nascimento"))
if find_birth_date:
    character_div_content = find_birth_date.find_parent("div")

    character_ems = character_div_content.find_all("em")

    character_data = {}
    for i in character_ems:
        text = i.get_text(strip=True)
        if ":" in text:
            key, value = text.split(":")
            character_data[key.strip()] = value.strip()
character_data

# %%
