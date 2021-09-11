"""
This is the User class that will represent all the users in the system and store their information
and access levels.
"""
from typing import List

from password import Password
from access_level import AccessLevel


class User:
    name: str = ""
    username: str = ""
    password: Password = Password()
    access_level = AccessLevel.Guest

    def __init__(self, name: str, username: str, password: Password, access_level: AccessLevel):
        self.name = name
        self.username = username
        self.password = password
        self.access_level = access_level

    @staticmethod
    def build_user_from_csv(user_data: List[str]):
        """Return a User object based on the string list extracted from the csv file storing users.
        All values except full name will have whitespace stripped.
        :param user_data: List of strings from the parsed csv row
        :return: User object created from the csv row.
        """

        if len(user_data) != 4:
            print(f'Invalid number of parameters provided to create User object! Expected 4, got {len(user_data)}')
            return

        full_name: str = user_data[0]
        username: str = user_data[1].replace(' ', '')
        password: Password = Password(user_data[2].replace(' ', ''))
        access_level_string: str = user_data[3].replace(' ', '')

        if access_level_string not in [level.value for level in AccessLevel]:
            print(f'Invalid access level! Excepted one of: {[level.value for level in AccessLevel]}, got '
                  f'{access_level_string}')
        else:
            return User(full_name, username, password, AccessLevel(access_level_string))

    def __repr__(self):
        return f'Name: {self.name}, Username: {self.username}, Password: {self.password}, ' \
               f'Access Level: {self.access_level};'
