# %%
from backend.scraper import get_character_list
from bs4 import BeautifulSoup
import re


def get_all_characters():
    html = get_character_list()
    if html == "Error":
        print("Erro na requisição, verificar se o nome do personagem está correto")

    soup = BeautifulSoup(html, features="html.parser")

    def get_names_by_letters(soup):
        letter = soup.find("h3", string="A")
        return letter

    return get_names_by_letters(soup)


get_all_characters()
