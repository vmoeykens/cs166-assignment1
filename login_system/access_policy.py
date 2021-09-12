"""
This class defines a structure so that sub-programs can have access policies determining who can access
different areas of the program.
"""
from typing import List

import login_system.access_level as access_level


class AccessPolicy:
    """
    Manages what levels can access something within this policy and performs validation on a requesting level.
    """
    def __init__(self):
        self.valid_levels: List[access_level.AccessLevel] = []
        self.valid_levels.append(access_level.AccessLevel.Admin)

    def add_level(self, level: access_level.AccessLevel):
        """
        Adds a new level to the access policy.
        :param level: Access level to add to this policy.
        """
        if level not in self.valid_levels:
            self.valid_levels.append(level)

    def validate(self, requesting_level: access_level.AccessLevel) -> bool:
        """
        Check to see if the level requesting access is within the access policy and should be allowed.
        :param requesting_level: Level requesting
        :return: Bool of whether or not the level is allowed.
        """
        return requesting_level in self.valid_levels

    def __repr__(self):
        levels_string = ""
        for level in self.valid_levels:
            levels_string += f"{level},"
        return levels_string
