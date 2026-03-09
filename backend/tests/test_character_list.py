import unittest
from unittest.mock import patch

from backend.parsers.character_list import get_all_characters


CHARACTER_LIST_HTML = """
<html>
  <body>
    <h3>A</h3>
    <p>
      <a href="/personagens/ada-wong/">Ada Wong</a>
      <a href="/personagens/albert-wesker/">Albert Wesker</a>
    </p>

    <h3>B</h3>
    <p>
      <a href="/personagens/barry-burton/">Barry Burton</a>
    </p>
  </body>
</html>
"""


class TestCharacterList(unittest.TestCase):
    @patch("backend.parsers.character_list.get_character_list")
    def test_returns_character_list_with_name_and_param(self, mock_get_character_list):
        mock_get_character_list.return_value = CHARACTER_LIST_HTML

        result = get_all_characters()

        self.assertEqual(
            result,
            [
                {"name": "Ada Wong", "param": "ada-wong"},
                {"name": "Albert Wesker", "param": "albert-wesker"},
                {"name": "Barry Burton", "param": "barry-burton"},
            ],
        )

    @patch("backend.parsers.character_list.get_character_list")
    def test_returns_empty_list_when_no_letters_are_found(
        self, mock_get_character_list
    ):
        mock_get_character_list.return_value = "<html><body></body></html>"

        result = get_all_characters()

        self.assertEqual(result, [])
