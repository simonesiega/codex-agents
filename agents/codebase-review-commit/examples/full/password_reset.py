import secrets
import time

TOKENS = {}


def create_reset_token(email):
    token = secrets.token_hex(16)
    TOKENS[email] = {
        "token": token,
        "created_at": time.time(),
    }
    return token


def reset_password(email, token, new_password):
    saved = TOKENS.get(email)
    if saved is None:
        return False

    if saved["token"] != token:
        return False

    print(f"Password reset for {email}: {new_password}")
    TOKENS.pop(email)
    return True
