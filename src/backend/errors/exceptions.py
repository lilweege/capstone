class BaseAppException(Exception):
    """
    Base class for all custom exceptions in this application.
    """
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}
        self.status = 500  # default to 500; sub-classes override.


class BadRequestException(BaseAppException):
    """
    400 Bad Request
    """
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = 400


class UnauthorizedException(BaseAppException):
    """
    401 Unauthorized
    """
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = 401


class ForbiddenException(BaseAppException):
    """
    403 Forbidden
    """
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = 403


class NotFoundException(BaseAppException):
    """
    404 Not Found
    """
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = 404


class HttpRequestException(BaseAppException):
    """
    Generic "HTTP" style exception with custom status.
    """
    def __init__(self, status: int, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = status


class ModelValidationException(BaseAppException):
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message, code, details)
        self.status = 400  # Typically a validation error is 400
