""" This module contains the exceptions raised by the Open Pinball DB API client """

class OpdbError(Exception):
    """Base class for Opdb exceptions"""

class OpdbMissingApiKey(OpdbError):
    """ Raised when calling private endpoints without an API key"""

class OpdbHTTPError(OpdbError):
    """ Raised when an HTTP error occurs"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

class OpdbTimeoutError(OpdbError):
    """ Raised when a timeout error occurs """
