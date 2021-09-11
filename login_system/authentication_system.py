"""
This class represents the Authentication system as a whole
"""
import csv
from typing import Tuple, Dict

from password import Password
from user import User


class AuthSystem:
    user_map: Dict[str, User] = {}
    program_list = []

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
                        if temp_user.username not in self.user_map:
                            self.user_map[temp_user.username] = temp_user
                        else:
                            print(f"Username {temp_user.username} already exists!")
        except OSError as e:
            print(f'Error parsing file {file_path}. OS returned {e}.')

    def print_users(self):
        """Prints out all current users in the system."""
        for username in self.user_map:
            print(self.user_map[username])

    def validate_user(self, username: str) -> bool:
        return username in self.user_map

    def validate_password(self, username: str, password: Password) -> bool:
        return self.user_map[username].password == password

    def prompt_and_validate_user(self) -> str:
        username: str = input("Username: ")
        while not self.validate_user(username):
            print(f"No user named {username}!")
            username = input("Username: ")
        return username

    def prompt_and_validate_password(self, username: str) -> Password:
        password: Password = Password(input("Password: "))
        while not self.validate_password(username, password):
            print(f"Invalid password!")
            password = Password(input("Password: "))
        return password

    def run_login_prompt(self):
        username: str = self.prompt_and_validate_user()
        password: Password = self.prompt_and_validate_password(username)

    def run(self):
        self.run_login_prompt()
        print("Login successful!")
