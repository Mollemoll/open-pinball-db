class OpdbError(Exception):
    """Base class for Opdb exceptions"""
    pass

class OpdbMissingApiKey(OpdbError):
    """ Raised when calling private endpoints without an API key"""
    pass
