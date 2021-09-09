"""
This class represents the Authentication system as a whole
"""
from typing import List

from user import User

UserList = List[User]


class AuthSystem:
    user_list: UserList = []
