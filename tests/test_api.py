import unittest
import requests
from pyjourney import MIDJOURNEY_USERID
from pyjourney import MidjourneyAPI

#  Test class for MidjourneyAPI


class TestMidjourneyAPI(unittest.TestCase):

    def setUp(self):

        self.api = MidjourneyAPI(user_id=MIDJOURNEY_USERID)

    def test_get_session_from_env(self):
        self.assertIsInstance(
            self.api.get_session_from_env(),
            requests.Session)

    def test_recent_jobs(self):
        result: requests.Response = self.api.recent_jobs()
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.headers["Content-Type"],
            "application/json; charset=utf-8")
