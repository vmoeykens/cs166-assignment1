"""
This class represents the Authentication system as a whole
"""
import csv
from typing import List

from user import User

UserList = List[User]


class AuthSystem:
    user_list: UserList = []

    def __init__(self):
        pass

    def parse_user_file(self, file_path: str):
        print(f'Parsing user file {file_path}.')
        try:
            with open(file_path, 'r') as user_file:
                reader = csv.reader(user_file)
                for row, user in enumerate(reader):
                    if row != 0 and user:
                        temp_user = User.build_user_from_csv(user)
                        print(f"Created user | {temp_user}")
                        self.user_list.append(temp_user)
        except OSError as e:
            print(f'Error parsing file {file_path}. OS returned {e}.')

    def print_users(self):
        """Prints out all current users in the system."""
        for user in self.user_list:
            print(user)
