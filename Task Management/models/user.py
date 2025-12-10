from .base import BaseEntity

class User(BaseEntity):
    def _init_(self, username: str, full_name: str):
        super()._init_()
        self._username = username
        self._full_name = full_name
        self._email = None

    # encapsulation via properties
    @property
    def username(self):
        return self._username

    @property
    def full_name(self):
        return self._full_name

    @property
    def email(self):
        return self._email

    def set_email(self, email: str):
        # simple validation
        if "@" not in email:
            raise ValueError("Invalid email")
        self._email = email

    def _repr_(self):
        return f"User({self._username})"