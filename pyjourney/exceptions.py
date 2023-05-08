# Exceptions for pyjourney
#


class PyJourneyException(Exception):
    """Base class for exceptions in this module."""
    pass


class SessionException(PyJourneyException):
    """Exception raised for errors in the session.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)
