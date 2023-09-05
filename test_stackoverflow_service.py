import unittest
from unittest.mock import patch
from stackoverflow_service import fetch_data_from_api
from stackoverflow_service import preprocessing_data
from stackoverflow_service import answer_questions
from stackoverflow_service import less_viewed_question
from stackoverflow_service import newest_oldest_question
from stackoverflow_service import most_reputation_owner_question
from test_mocks.objects_mocks import *
from unittest.mock import Mock
import json
import requests
import pandas as pd


class MyTestCase(unittest.TestCase):

    @patch("requests.get")
    def test_successful_request(self, mock_get):
        # Mocking a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = get_response_mock
        mock_get.return_value = mock_response

        result = fetch_data_from_api()
        self.assertEqual(result, json.loads(get_response_mock))

    @patch("requests.get")
    def test_http_error(self, mock_get):
        # Mocking a response using a real Response object
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response._content = "Not Found"

        http_error = requests.exceptions.HTTPError()
        http_error.response = Mock()
        http_error.response.status_code = 404
        mock_response.raise_for_status.side_effect = http_error

        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            fetch_data_from_api()
        s = str(context.exception)
        self.assertTrue("HTTP error: 404" in str(context.exception))

    def test_preprocessing_data(self):
        data_mock = json.loads(get_response_mock)
        df = preprocessing_data(data_mock)
        df_expected = pd.DataFrame(preprocessing_data_mock)

        pd.testing.assert_frame_equal(df, df_expected)

    def test_answer_questions(self):
        data_mock = pd.DataFrame(preprocessing_data_mock)
        df = answer_questions(data_mock)
        result = df.value_counts("is_answered")
        self.assertEqual(result.to_dict(), answer_questions_mock)

    def test_less_viewed_question(self):
        data_mock = pd.DataFrame(preprocessing_data_mock)
        result = less_viewed_question(data_mock)
        self.assertEqual(result.to_dict(), less_viewed_question_mock)

    def test_newest_oldest_question(self):
        data_mock = pd.DataFrame(preprocessing_data_mock)
        result = newest_oldest_question(data_mock)
        self.assertEqual(result.to_dict(), newest_oldest_question_mock)

    def test_most_reputation_owner_question(self):
        data_mock = pd.DataFrame(preprocessing_data_mock)
        result = most_reputation_owner_question(data_mock)
        self.assertEqual(result.to_dict(), most_reputation_owner_question_mock)


if __name__ == '__main__':
    unittest.main()
