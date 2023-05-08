import unittest
import requests
from pyjourney import MIDJOURNEY_USERID
from pyjourney import GetJobsArgs

#  Test class for MidjourneyAPI


class TestGetJobsArgs(unittest.TestCase):

    def test_init(self):
        args = GetJobsArgs()
        self.assertIsInstance(
            args,
            GetJobsArgs)

    def test_user_id(self):
        args = GetJobsArgs(user_id=MIDJOURNEY_USERID)
        self.assertEqual(args.user_id, MIDJOURNEY_USERID)
        d = args.to_dict()
        self.assertEqual(d['user_id'], MIDJOURNEY_USERID)
