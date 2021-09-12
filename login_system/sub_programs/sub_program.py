"""
This is the abstract class that all sub-programs will inherit. It defines the minimum implementation
for a sub-program.
"""
from login_system.access_policy import AccessPolicy
from login_system.access_level import AccessLevel
from login_system.user import User


class SubProgram:
    access_policy: AccessPolicy = None
    sub_program_name: str = ""

    def run_program(self, accessing_user: User):
        pass

    def validate_access_policy(self, accessing_user: User) -> bool:
        if not self.access_policy.validate(accessing_user.access_level):
            print(f"This program requires access level(s): {self.access_policy}! requesting user is only "
                  f"{accessing_user.access_level}.")
            return False
        else:
            return True


class TimeReporting(SubProgram):
    sub_program_name: str = "Time Reporting"

    def __init__(self):
        self.access_policy = AccessPolicy()
        self.access_policy.add_level(AccessLevel.User)

    def run_program(self, accessing_user: User):
        if super(TimeReporting, self).validate_access_policy(accessing_user):
            print(f"You have reached the time reporting program!\n")

    def __repr__(self):
        return self.sub_program_name


class Accounting(SubProgram):
    sub_program_name: str = "Accounting"

    def __init__(self):
        self.access_policy = AccessPolicy()
        self.access_policy.add_level(AccessLevel.User)

    def run_program(self, accessing_user: User):
        if super(Accounting, self).validate_access_policy(accessing_user):
            print(f"You have reached the accounting program!\n")

    def __repr__(self):
        return self.sub_program_name


class UserManagement(SubProgram):
    sub_program_name: str = "User Management"

    def __init__(self):
        self.access_policy = AccessPolicy()

    def run_program(self, accessing_user: User):
        if super(UserManagement, self).validate_access_policy(accessing_user):
            print(f"You have reached the User Management program!\n")

    def __repr__(self):
        return self.sub_program_name


class DataViewer(SubProgram):
    sub_program_name: str = "Data Viewer"

    def __init__(self):
        self.access_policy = AccessPolicy()
        self.access_policy.add_level(AccessLevel.User)
        self.access_policy.add_level(AccessLevel.Guest)

    def run_program(self, accessing_user: User):
        if super(DataViewer, self).validate_access_policy(accessing_user):
            print(f"You have reached the Data Viewer program!\n")

    def __repr__(self):
        return self.sub_program_name
