# PyJourney

A python module for calling the Midjourney API.

## Installation

```bash
pip install pyjourney
```

## Usage

```python
from pyjourney import MidjourneyAPI


api = MidjourneyAPI()        #Loads your cookie and userId from the .env file  (required for now.)
request = api.recent_jobs()  # Defaults to fetching the most recent 35 jobs you've done.
print(request.status_code)
```
