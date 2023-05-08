from dotenv import load_dotenv
import requests
import logging
import os

from pyjourney.exceptions import SessionException
from pyjourney.models import GetJobsArgs


class MidjourneyAPI:
    """Class for interacting with the Midjourney API
    """

    def __init__(self, user_id: str = None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.debug("MidjourneyAPI initialized")

        self.root_url = "https://www.midjourney.com"

        self.headers = {
            "authority": "www.midjourney.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "dnt": "1",
            "referer": "https://www.midjourney.com/app/"
        }

        self.session = self.get_session_from_env()
        self.user_id = user_id

    def get_session_from_env(self, env_var: str = "MIDJOURNEY_COOKIE"):
        """Returns a session from the environment variables

        Arguments:
            env_var {str} -- The name of the environment variable us for sessions

        Returns:
            requests.Session -- The session

        Raises:
            SessionException -- If the environment variable is not found
        """

        cookie_string = os.getenv(env_var)

        if not cookie_string:
            raise SessionException(
                "Session file not found and no session in environment variables did you set the MIDJOURNEY_COOKIE environment variable?"
            )

        # https://stackoverflow.com/questions/17224054/how-to-add-a-cookie-to-the-cookiejar-in-python-requests-library
        cookiejar_dict = {}
        for cookie_string in cookie_string.split(";"):
            # maxsplit=1 because cookie value may have "="
            cookie_key, cookie_value = cookie_string.strip().split("=", maxsplit=1)
            cookiejar_dict[cookie_key] = cookie_value

        if cookiejar_dict == {}:
            raise SessionException(
                "Session file found, but no cookies in file")

        session = requests.Session()
        session.cookies.update(cookiejar_dict)
        self.logger.debug("Session loaded from environment variables")
        return session

    def recent_jobs(self, args: GetJobsArgs = None) -> requests.Response:
        """
        Returns the recent jobs from the Midjourney API, this is the same as your homepage when logging in on the website and sorting by "all" instead of grid or upscales

        Arguments:
            args {GetJobsArgs} -- The arguments to pass to the API, leave blank to use the default arguments

        Returns:
            requests.Response -- The response from the API
        """
        url = self.root_url + "/api/app/recent-jobs"

        if not args:
            args = GetJobsArgs(user_id=self.user_id)

        self.logger.debug("Requesting " + url)
        response = self.session.get(
            url, headers=self.headers, params=args.to_dict())

        if response.status_code == 429:
            raise Exception("Too many requests")

        while response.status_code == 302 or response.status_code == 308:
            self.logger.debug("Redirecting to " + response.headers["Location"])
            response = self.session.get(response.headers["Location"])

            if response.status_code == 429:
                raise Exception("Too many requests")

        self.logger.debug("Response: " + str(response.status_code))
        return response


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    # Load the .env file
    if not load_dotenv():
        logger.warning("No .env file found")
        exit(1)

    api = MidjourneyAPI()

    request = api.recent_jobs()
    print(request.status_code)
