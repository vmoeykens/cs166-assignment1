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
        """
        Parses a given csv file containing all the users in the system. Will validate that all usernames are unique.
        If a non-unique username is found, only the first sequentially found username will be added to the system.
        :param file_path: Relative or absolute path to the csv file containing the user list.
        """
        print(f'Parsing user file {file_path}.')
        try:
            with open(file_path, 'r') as user_file:
                reader = csv.reader(user_file)
                for row, user in enumerate(reader):
                    if row != 0 and user:
                        temp_user = User.build_user_from_csv(user)
                        if temp_user:
                            print(f"Created user | {temp_user}")
                            if temp_user.username not in self.user_map:
                                self.user_map[temp_user.username] = temp_user
                            else:
                                print(f"Username {temp_user.username} already exists!")
                        else:
                            print(f"Unable to create User object")
        except OSError as e:
            print(f'Error parsing file {file_path}. OS returned {e}.')

    def print_users(self):
        """Prints out all current users in the system."""
        for username in self.user_map:
            print(self.user_map[username])

    def validate_user(self, username: str) -> bool:
        """
        Validates whether or not a user is valid in the system.
        :param username: String username of the user to check
        :return: Bool representing whether or not the uesr is valid in the system
        """
        return username in self.user_map

    def validate_password(self, username: str, password: Password) -> bool:
        """
        Checks to see if a password is valid for a given username. We assume the user has already been validated.
        :param username: String username of the user to check
        :param password: String password of the password to check
        :return: Bool representing whether or not the password is valid for the given user.
        """
        return self.user_map[username].password == password

    def prompt_and_validate_user(self) -> str:
        """
        Prompts for a username and re-prompts until one is valid.
        :return: String of the valid username selected
        """
        username: str = input("Username: ")
        while not self.validate_user(username):
            print(f"No user named {username}!")
            username = input("Username: ")
        return username

    def prompt_and_validate_password(self, username: str) -> Password:
        """
        Prompts for a valid password for the given user. Re-prompts until the correct password is selected.
        :param username: String username to validate a password against.
        :return: Valid password object for the given user
        """
        password: Password = Password(input("Password: "))
        while not self.validate_password(username, password):
            print(f"Invalid password!")
            password = Password(input("Password: "))
        return password

    def run_login_prompt(self):
        """
        Runs the login prompt until a valid username and password combination is selected.
        """
        username: str = self.prompt_and_validate_user()
        password: Password = self.prompt_and_validate_password(username)

    def run(self):
        """
        Runs the main program (login, and then menu for sub-programs)
        """
        self.run_login_prompt()
        print("Login successful!")
