"""
This class represents the Authentication system as a whole
"""
import csv
from typing import Tuple, Dict

from login_system.password import Password
from login_system.user import User
from login_system.sub_programs.sub_program import TimeReporting, Accounting, UserManagement, DataViewer

SUB_PROGRAM_MENU_OFFSET: int = 2
EXIT_SELECTION_MENU_OFFSET: int = 1


class AuthSystem:
    """
    Authentication system that manages users and subprograms, and handles user input for navigating the system.
    """
    user_map: Dict[str, User] = {}
    program_list = []
    valid_user_file: bool = False
    user_logged_in: bool = False
    user: User = None

    def __init__(self):
        time_reporting = TimeReporting()
        accounting = Accounting()
        user_management = UserManagement()
        data_viewer = DataViewer()
        self.program_list = [time_reporting, accounting, user_management, data_viewer]

    def parse_user_file(self, file_path: str, debug: bool):
        """
        Parses a given csv file containing all the users in the system. Will validate that all usernames are unique.
        If a non-unique username is found, only the first sequentially found username will be added to the system.
        :param debug: Boolean to determine whether or not to print out users as they are added
        :param file_path: Relative or absolute path to the csv file containing the user list.
        """
        if debug:
            print(f'Parsing user file {file_path}.')
        try:
            with open(file_path, 'r') as user_file:
                reader = csv.reader(user_file)
                for row, user in enumerate(reader):
                    if row != 0 and user:
                        temp_user = User.build_user_from_csv(user)
                        if temp_user:
                            if debug:
                                print(f"Created user | {temp_user}")
                            if temp_user.username not in self.user_map:
                                self.user_map[temp_user.username] = temp_user
                            else:
                                print(f"Username {temp_user.username} already exists!")
                        else:
                            print(f"Unable to create User object")
            self.valid_user_file = True
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

        self.user_logged_in = True
        self.user = self.user_map[username]

        return password

    def run_login_prompt(self):
        """Runs the login prompt until a valid username and password combination is selected."""
        username: str = self.prompt_and_validate_user()
        password: Password = self.prompt_and_validate_password(username)

    def print_menu_options(self):
        """Prints all the sub-program names to select."""
        print('1. Exit')
        for i, sub_program in enumerate(self.program_list):
            print(f'{i + SUB_PROGRAM_MENU_OFFSET}. {sub_program}')
        print('\n')

    def run_main_menu(self):
        """Runs the main menu to select different sub-programs until quit is selected."""
        if not self.user_logged_in:
            print("User not logged in! Exiting.")
            return

        menu_selection: int = 0
        while menu_selection != EXIT_SELECTION_MENU_OFFSET:
            self.print_menu_options()
            menu_selection: int = int(input('Select a menu option: '))
            if menu_selection < EXIT_SELECTION_MENU_OFFSET or menu_selection > len(self.program_list) + \
                    EXIT_SELECTION_MENU_OFFSET:
                print('Invalid selection!\n')
            elif menu_selection == EXIT_SELECTION_MENU_OFFSET:
                pass
            else:
                self.program_list[menu_selection - SUB_PROGRAM_MENU_OFFSET].run_program(self.user)
        print('Exiting!')

    def run(self):
        """Runs the main program (login, and then menu for sub-programs)."""
        if self.valid_user_file:
            print("Welcome to the company intranet!\nPlease Login\n")
            self.run_login_prompt()
            print("Login successful!")
            self.run_main_menu()
        else:
            print("User file was not valid! Exiting.")
