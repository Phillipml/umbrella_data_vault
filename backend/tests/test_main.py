import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


class TestCharactersList(unittest.TestCase):
    @patch("backend.main.get_all_characters")
    def test_characters_list_returns_200_and_list(self, mock_get_all):
        mock_get_all.return_value = [
            {"name": "Ada Wong", "param": "ada-wong"},
            {"name": "Leon Kennedy", "param": "leon-kennedy"},
        ]

        response = client.get("/characters_list")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["name"], "Ada Wong")
        self.assertEqual(response.json()[0]["param"], "ada-wong")
        mock_get_all.assert_called_once()

    @patch("backend.main.get_all_characters")
    def test_characters_list_returns_empty_list_when_no_characters(self, mock_get_all):
        mock_get_all.return_value = []

        response = client.get("/characters_list")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


class TestCharacterBio(unittest.TestCase):
    @patch("backend.main.character_data")
    def test_character_bio_returns_200_and_data(self, mock_character_data):
        mock_character_data.return_value = {
            "Name": "Ada Wong",
            "Img": "https://example.com/ada.jpg",
            "Bio": "Uma espiã misteriosa.",
        }

        response = client.get("/character-bio/ada-wong")

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["Name"], "Ada Wong")
        self.assertIn("Img", data)
        self.assertIn("Bio", data)
        mock_character_data.assert_called_once_with("ada-wong")

    @patch("backend.main.character_data")
    def test_character_bio_returns_null_when_character_not_found(
        self, mock_character_data
    ):
        mock_character_data.return_value = None

        response = client.get("/character-bio/personagem-inexistente")

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json())
        mock_character_data.assert_called_once_with("personagem-inexistente")
