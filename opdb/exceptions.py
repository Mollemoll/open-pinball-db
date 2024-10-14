class OpdbError(Exception):
    """Base class for Opdb exceptions"""
    pass

class OpdbMissingApiKey(OpdbError):
    """ Raised when calling private endpoints without an API key"""
    pass

class OpdbHTTPError(OpdbError):
    """ Raised when an HTTP error occurs"""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
