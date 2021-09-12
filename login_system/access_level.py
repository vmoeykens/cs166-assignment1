"""
This sets up various access levels that a user may have.
"""
import enum


class AccessLevel(enum.Enum):
    """
    Enum for the valid access levels in this system.
    """
    Guest = "guest"
    User = "user"
    Admin = "admin"
