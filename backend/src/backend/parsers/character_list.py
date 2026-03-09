# %%
from backend.scraper import get_character_list
from bs4 import BeautifulSoup
import re
import string


def get_all_characters():
    html = get_character_list()
    if html == "Error":
        print("Erro na requisição, verificar se o nome do personagem está correto")

    soup = BeautifulSoup(html, features="html.parser")

    def get_names_by_letters(soup):
        characters_list = []
        for letter_tag in string.ascii_uppercase:
            letter = soup.find("h3", string=letter_tag)
            if not letter:
                continue
            find_p_tag = letter.find_next_sibling("p")
            if not find_p_tag:
                return "Erro ao encontrar tag P"
            a_tag = find_p_tag.find_all("a")

            for i in a_tag:
                name = i.get_text()
                param = i.get("href").split("/")[-2]

                characters_list.append({"name": name, "param": param})
        return characters_list

    return get_names_by_letters(soup)


get_all_characters()
