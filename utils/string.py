import random
import string
import uuid


def truncate_string(s, length, suffix=""):
    """
    truncate string to specific length
    """
    if length >= len(s):
        return s

    if not suffix:
        return f"{s[:length]}"

    return f"{s[:length - len(suffix)]}{suffix}"


def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_unique_id():
    return uuid.uuid4().hex