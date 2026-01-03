import os
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class AES256:

    def __init__(self):
        """
        key 길이: 32 bytes (AES-256)
        """
        self.key = base64.b64decode("0rLxSECieB03RG8UBESHRyoKyNFL4fL6PqDXzxKyPZE=")
        self.backend = default_backend()


    def encrypt(self, plain_text: str) -> str:
        iv = os.urandom(16)  # CBC 모드 IV는 16바이트
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(iv),
            backend=self.backend
        )

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text.encode()) + padder.finalize()

        encryptor = cipher.encryptor()
        encrypted = encryptor.update(padded_data) + encryptor.finalize()

        # iv + ciphertext 를 base64로 인코딩
        return base64.b64encode(iv + encrypted).decode()


    def decrypt(self, cipher_text: str) -> str:
        decoded = base64.b64decode(cipher_text)

        iv = decoded[:16]
        encrypted = decoded[16:]

        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(iv),
            backend=self.backend
        )

        decryptor = cipher.decryptor()
        padded_plain = decryptor.update(encrypted) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        plain = unpadder.update(padded_plain) + unpadder.finalize()

        return plain.decode()


if __name__ == "__main__":
    aes256 = AES256()
    result1 = aes256.encrypt("최종규")

    result2 = aes256.decrypt(result1)
    print(result2)
