"""
This sets up various access levels that a user may have.
"""
import enum


class AccessLevel(enum.Enum):
    Guest = "guest"
    User = "user"
    Admin = "admin"
