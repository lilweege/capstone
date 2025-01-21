import json
from errors.exceptions import BaseAppException
from constants.env_variables import AppConfig

class ErrorContent:
    """
    A Python version of your TypeScript "ErrorContent" concept.
    It takes an exception and builds a structured dict for JSON responses.
    """

    def __init__(self, *, status: int, code: str, message: str, details: dict):
        self.type = "Error"
        self.target = AppConfig.APP_NAME
        self.status = status
        self.code = code
        self.message = message
        self.ext = details 
        self.raw = {}

    @classmethod
    def from_exception(cls, exc: BaseAppException) -> "ErrorContent":
        """
        Build an ErrorContent from one of our custom exceptions.
        """
        return cls(
            status=exc.status,
            code=exc.code if exc.code else "UNKNOWN",
            message=exc.message,
            details=exc.details
        )

    def get_summary(self) -> dict:
        """
        Return only the main fields without raw details.
        """
        return {
            "type": self.type,
            "target": self.target,
            "status": self.status,
            "code": self.code,
            "message": self.message,
            "ext": self.ext
        }

    def get_details(self) -> dict:
        """
        Include raw as well.
        """
        data = self.get_summary()
        data["raw"] = self.raw
        return data

    def to_json_str(self) -> str:
        """
        Return the full details as a JSON string, if needed.
        """
        return json.dumps(self.get_details())
