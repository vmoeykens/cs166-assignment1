"""
Main entrypoint to the application.
"""
from authentication_system import AuthSystem


def main():
    auth_system: AuthSystem = AuthSystem()
    auth_system.parse_user_file('data/users.csv')
    auth_system.print_users()
    auth_system.run()


if __name__ == "__main__":
    main()
