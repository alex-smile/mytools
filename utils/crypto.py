import base64
import hashlib
from typing import Tuple

from Crypto.PublicKey import RSA


class KeyGenerator:

    @staticmethod
    def generate_rsa_key(length=2048) -> Tuple:
        """生成一个新的密钥"""
        key = RSA.generate(length)
        private_key = key.exportKey()
        public_key = key.publickey().exportKey()
        return private_key, public_key


def calculate_fingerprint(content):
    """For specification, see RFC4716, section 4"""
    key = base64.b64decode("".join(content.splitlines()[1:-1]).encode("ascii"))
    fp_plain = hashlib.md5(key).hexdigest()
    return ":".join(a + b for a, b in zip(fp_plain[::2], fp_plain[1::2]))