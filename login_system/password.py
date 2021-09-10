"""
This class represents a user's password, for now this is just plaintext.
"""


class Password:
    value: str = ""

    def __init__(self, password_value : str = ""):
        self.value = password_value

    def __repr__(self):
        return f"{self.value}"
