import unittest
from unittest.mock import Mock, patch

from backend.scraper import get_character_content, get_character_list


class TestScraper(unittest.TestCase):
    @patch("backend.scraper.requests.get")
    def test_get_character_content_returns_html_when_request_succeeds(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html>ok</html>"
        mock_get.return_value = mock_response

        result = get_character_content("ada-wong")

        self.assertEqual(result, "<html>ok</html>")
        mock_get.assert_called_once()

    @patch("backend.scraper.requests.get")
    def test_get_character_content_returns_error_when_request_fails(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = ""
        mock_get.return_value = mock_response

        result = get_character_content("ada-wong")

        self.assertEqual(result, "Error")

    @patch("backend.scraper.requests.get")
    def test_get_character_list_returns_html_when_request_succeeds(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html>lista</html>"
        mock_get.return_value = mock_response

        result = get_character_list()

        self.assertEqual(result, "<html>lista</html>")

    @patch("backend.scraper.requests.get")
    def test_get_character_list_returns_error_when_request_fails(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = ""
        mock_get.return_value = mock_response

        result = get_character_list()

        self.assertEqual(result, "Error")
