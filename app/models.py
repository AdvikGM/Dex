# app/models.py
import hashlib

class UserProfile:
    def __init__(self, username, password_raw, email, locked=False, attempts=0):
        self.username = username.strip()
        self.password_hashed = self.hash_string_data(password_raw.strip())
        self.email = email.strip()
        self.locked = locked
        self.attempts = attempts

    @staticmethod
    def hash_string_data(raw_text):
        return hashlib.sha256(raw_text.encode()).hexdigest()

    def to_dict(self):
        return {
            "password": self.password_hashed,
            "email": self.email,
            "locked": self.locked,
            "attempts": self.attempts
        }
