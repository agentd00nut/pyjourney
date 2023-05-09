# TODO:: Use pydantic to validate the data
# This is a class to hold the values for the get_jobs api call
class GetJobsArgs:

    def __init__(
            self,
            amount=1,
            dedupe=True,
            jobStatus="completed",
            orderBy="new",
            prompt="undefined",
            refreshApi="0",
            searchType="advanced",
            service="null",
            type="all",
            userId="",
            user_id_ranked_score="null",
            _ql="todo",
            _qurl="https://www.midjourney.com/app/"):
        self.amount = amount
        self.dedupe = dedupe
        self.jobStatus = jobStatus
        self.orderBy = orderBy
        self.prompt = prompt
        self.refreshApi = refreshApi
        self.searchType = searchType
        self.service = service
        self.type = type
        self.userId = userId
        self.user_id_ranked_score = user_id_ranked_score
        self._ql = _ql
        self._qurl = _qurl
        self._dict = self.to_dict()

    def __repr__(self) -> str:
        return str(self._dict)

    # A  to build this class from an already existing dictionary preferring keys from the given dictionary
    # It iterates over the given dictionary and sets the values of this class
    # to the values of the given dictionary
    @classmethod
    def from_dict(self, dict):
        for key in dict:
            setattr(self, key, dict[key])
        self._dict = self.to_dict()
        return self

    def to_dict(self):
        return {
            "amount": self.amount,
            "dedupe": self.dedupe,
            "jobStatus": self.jobStatus,
            "orderBy": self.orderBy,
            "prompt": self.prompt,
            "refreshApi": self.refreshApi,
            "searchType": self.searchType,
            "service": self.service,
            "type": self.type,
            "userId": self.userId,
            "user_id_ranked_score": self.user_id_ranked_score,
            "_ql": self._ql,
            "_qurl": self._qurl
        }
