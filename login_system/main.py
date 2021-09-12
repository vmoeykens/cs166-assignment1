"""
Main entrypoint to the application.
"""
import argparse
from login_system.authentication_system import AuthSystem


def main():
    parser = argparse.ArgumentParser(description='Run the authentication system')

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        dest='debug',
                        help='Print Debug output when loading users.'
                        )
    parser.add_argument('-f', '--file',
                        default='login_system/data/user_list.csv',
                        dest='file',
                        help='Path to users file. Default is login_system/data/user_list.csv',
                        type=str
                        )
    args = parser.parse_args()

    auth_system: AuthSystem = AuthSystem()
    auth_system.parse_user_file(args.file, args.debug)
    if args.debug:
        auth_system.print_users()

    auth_system.run()


if __name__ == "__main__":
    main()
