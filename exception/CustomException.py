from code.ResultCode import ResultCode


class CustomException(RuntimeError):
    def __init__(self, code: ResultCode, message: str | None = None):
        self.code = code
        self.message = message or code.value