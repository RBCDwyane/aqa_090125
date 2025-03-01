import os
import logging
import unittest
from unittest import mock
from homework_11 import log_event

class TestLogEvent(unittest.TestCase):

    @mock.patch("logging.getLogger")
    def test_log_event_success(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("player_one", "success")
        mock_logger.info.assert_called_with("Login event - Username: player_one, Status: success")
        mock_logger.error.assert_not_called()
        mock_logger.warning.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_expired(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("player_two", "expired")
        mock_logger.warning.assert_called_with("Login event - Username: player_two, Status: expired")
        mock_logger.info.assert_not_called()
        mock_logger.error.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_failed(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("player_three", "failed")
        mock_logger.error.assert_called_with("Login event - Username: player_three, Status: failed")
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_empty_username(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("", "success")
        mock_logger.error.assert_called_with("Спроба входу з порожнім іменем користувача.")
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_empty_status(self, mock_get_logger):
        # Мокаем сам логгер
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("player_one", "")
        mock_logger.error.assert_called_with("Не визначений статус користувача")
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_incorrect_username(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event(12345, "succes")
        mock_logger.error.assert_called_with("Некоректний тип даних")
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

    @mock.patch("logging.getLogger")
    def test_log_event_incorrect_status(self, mock_get_logger):
        mock_logger = mock.Mock()
        mock_get_logger.return_value = mock_logger

        log_event("player_one", 12345)
        mock_logger.error.assert_called_with("Некоректний тип даних")
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

if __name__ == "__main__":
    unittest.main()