# PyJourney

A python module for calling the Midjourney API to get job details and for creating jobs.

Currently just trying to fix [midjourney-graph](https://github.com/agentd00nut/midjourney-graph) and figured i'd break out the api calls into a module.

## TODO

- [ ] more than 35 jobs at a time.
- [ ] jobs by date range, type, and for other users
- [ ] get sepcific job details for a job and a list of jobs
- [ ] get the list of community jobs by hot, new, trending, etc.
- [ ] Searching for jobs by title, description, and tags

## Installation

```bash
pip install pyjourney
```

## Setup

Create a .env file in the root of your project and add the following:

```bash
MIDJOURNEY_COOKIE=your_cookie
MIDJOURNEY_USERID=your_userId
```

The userID should be the newer GUID version of the userid, not the old integer version.
The cookie can be taken from the cookie header in your browser when you're logged in to Midjourney for any request against the API.

## Usage

```python
from pyjourney import MidjourneyAPI


api = MidjourneyAPI()        #Loads your cookie and userId from the .env file  (required for now.)
request = api.recent_jobs()  # Defaults to fetching the most recent 35 jobs you've done.
print(request.status_code)  # request.json() should work if this is 200 :)
```
