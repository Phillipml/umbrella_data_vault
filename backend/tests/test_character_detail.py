import unittest
from unittest.mock import patch

from backend.parsers.character_detail import character_data


CHARACTER_HTML = """
<html>
  <body>
    <span>Personagens | Ada Wong</span>
    <div class="profile">
      <img src="https://img.example/ada.png" />
      <em>Ano de nascimento: 1974</em>
      <em>Altura: 1,70 m</em>
    </div>

    <h4>Biografia</h4>
    <p>Ada e uma espia misteriosa.</p>
    <p>Ela aparece em varios jogos.</p>
    <div>Fim</div>
  </body>
</html>
"""


CHARACTER_WITHOUT_BIRTH_DATE_HTML = """
<html>
  <body>
    <span>Personagens | Ada Wong</span>
    <h4>Biografia</h4>
    <p>Ada e uma espia misteriosa.</p>
  </body>
</html>
"""


class TestCharacterDetail(unittest.TestCase):
    @patch("backend.parsers.character_detail.get_character_content")
    def test_returns_character_data_when_html_is_valid(
        self, mock_get_character_content
    ):
        mock_get_character_content.return_value = CHARACTER_HTML

        result = character_data("ada-wong")

        self.assertEqual(result["Name"], "Ada Wong")
        self.assertEqual(result["Img"], "https://img.example/ada.png")
        self.assertEqual(result["Ano de nascimento"], "1974")
        self.assertEqual(result["Altura"], "1,70 m")
        self.assertEqual(
            result["Bio"],
            "Ada e uma espia misteriosa. Ela aparece em varios jogos.",
        )

    @patch("backend.parsers.character_detail.get_character_content")
    def test_returns_none_when_scraper_fails(self, mock_get_character_content):
        mock_get_character_content.return_value = "Error"

        result = character_data("ada-wong")

        self.assertIsNone(result)

    @patch("backend.parsers.character_detail.get_character_content")
    def test_returns_only_bio_when_birth_date_is_missing(
        self, mock_get_character_content
    ):
        mock_get_character_content.return_value = CHARACTER_WITHOUT_BIRTH_DATE_HTML

        result = character_data("ada-wong")

        self.assertEqual(result, {"Bio": "Ada e uma espia misteriosa."})
