import base64
import binascii

from Crypto.Cipher import AES
from Crypto.Util import Counter

from code.ResultCode import ResultCode
from exception.CustomException import CustomException


class AES256:
    alg = "AES-CTR"

    key = "lisztlisztlisztlisztlisztliszttt"
    iv = "lisztlisztlisztlisztli"

    def __init__(self):
        try:
            self.key_bytes = base64.b64decode(self.key)
            self.iv_bytes = base64.b64decode(self.iv)
            #self.key_bytes = self.b64decode_fix(self.key)
            #self.iv_bytes = self.b64decode_fix(self.iv)

            #CTR모드 Counter 생성
            self.counter = Counter.new(
                128,
                initial_value=int.from_bytes(self.iv_bytes, "big"),
            )
        except binascii.Error as e:
            raise CustomException(ResultCode.AES_ERROR) from e
            #raise RuntimeError("AES_FAIL") from e

    def encrypt(self, text: str) -> str:
        try:
            cipher = AES.new(
                self.key_bytes,
                AES.MODE_CTR,
                counter = self.counter
            )

            encrypted = cipher.encrypt(text.encode("utf-8"))
            return base64.b64encode(encrypted).decode("utf-8")
        except Exception as e:
            raise RuntimeError("AES_FAIL") from e



    def decrypt(self, cipher_text:str) -> str:
        try:
            cipher = AES.new(
                self.key_bytes,
                AES.MODE_CTR,
                counter = self.counter
            )

            decoded = base64.b64decode(cipher_text)
            decrypted = cipher.decrypt(decoded)
            return decrypted.decode("utf-8")

        except Exception as e:
            print("여기기기긱")
            print(e)
            raise RuntimeError("AES_FAIL") from e

    @staticmethod
    def b64decode_fix(s: str) -> bytes:

        print(len(s))
        print(len(s))
        s += "=" * (-len(s) % 4)
        print(s)
        return base64.b64decode(s)


if __name__ == "__main__":
    aes = AES256()

    plain_text = "hello-fastapi-aes-test"
    print("원문 : ", plain_text)

    encrypted = aes.encrypt(plain_text)
    print("암호화 : ", encrypted)

    decrypted = aes.decrypt(encrypted)
    print("복호화 : ", decrypted)

    assert plain_text == decrypted
    print("테스트 성공")

