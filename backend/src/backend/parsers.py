# %%
from bs4 import BeautifulSoup
import re
from backend.scraper import html

soup = BeautifulSoup(html, features="html.parser")
soup.find("div", class_="td-page-content")

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
