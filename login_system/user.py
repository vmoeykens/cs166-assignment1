"""
This is the User class that will represent all the users in the system and store their information
and access levels.
"""
from password import Password
from access_level import AccessLevel


class User:

    username: str = ""
    password: Password = Password()
    access_level = AccessLevel.Guest

    def __init__(self, username: str, password: Password, access_level: AccessLevel):
        self.username = username
        self.password = password
        self.access_level = access_level
