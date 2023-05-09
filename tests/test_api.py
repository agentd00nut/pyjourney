import unittest
from pyjourney import MIDJOURNEY_USERID, MidjourneyAPI
import requests


#  Test class for MidjourneyAPI


class TestMidjourneyAPI(unittest.TestCase):

    def setUp(self):
        self.api = MidjourneyAPI(user_id=MIDJOURNEY_USERID)

    def test_get_session_from_env(self):
        self.assertIsInstance(
            self.api._get_session_from_env(),
            requests.Session)

    def test_recent_jobs(self):
        result: requests.Response = self.api.recent_jobs()
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.headers["Content-Type"],
            "application/json; charset=utf-8")
        jobs = result.json()
        self.assertEqual(len(jobs), 1)

    def test_job_status(self):
        result = self.api.recent_jobs()
        
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 200)
        
        jobs = [job['id'] for job in result.json()]
        result = self.api.job_status([jobs[0]])
        
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 200) 


if __name__ == "__main__":
    unittest.main()