from enum import StrEnum


class ResultCode(StrEnum):
    # Success
    SUCCESS = ("SUCCESS", "요청이 성공적으로 처리되었습니다.")
    CREATED = ("CREATED", "리소스가 생성되었습니다.")
    UPDATED = ("UPDATED", "리소스가 수정되었습니다.")
    DELETED = ("DELETED", "리소스가 삭제되었습니다.")

    # Client Error
    INVALID_PARAM = ("INVALID_PARAM", "요청 파라미터가 올바르지 않습니다.")
    MISSING_PARAM = ("MISSING_PARAM", "필수 파라미터가 누락되었습니다.")
    DUPLICATE_RESOURCE = ("DUPLICATE_RESOURCE", "이미 존재하는 리소스입니다.")
    RESOURCE_NOT_FOUND = ("RESOURCE_NOT_FOUND", "요청한 리소스를 찾을 수 없습니다.")
    UNAUTHORIZED = ("UNAUTHORIZED", "인증이 필요합니다.")
    FORBIDDEN = ("FORBIDDEN", "접근 권한이 없습니다.")

    # Business Error
    BUSINESS_ERROR = ("BUSINESS_ERROR", "비즈니스 처리 중 오류가 발생했습니다.")
    USER_ALREADY_EXISTS = ("USER_ALREADY_EXISTS", "이미 존재하는 사용자입니다.")

    # Server Error
    INTERNAL_ERROR = ("INTERNAL_ERROR", "서버 내부 오류가 발생했습니다.")
    DATABASE_ERROR = ("DATABASE_ERROR", "데이터베이스 처리 중 오류가 발생했습니다.")
    AES_ERROR = ("AES_ERROR", "암호화 처리 중 오류가 발생했습니다.")

    # User
    USER_EXISTS = ("USER_EXISTS", "사용자가 존재합니다.")
    NOT_EXISTS = ("NOT_EXISTS", "대상이 존재하지 않습니다.")

    def __new__(cls, code:str, message:str):
        obj = str.__new__(cls, code)
        obj._value_ = code
        obj.message = message
        return obj




