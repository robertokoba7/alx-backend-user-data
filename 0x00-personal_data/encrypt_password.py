#!/usr/bin/env python3
"""
passwords encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ 
    Returns a byte string: salted, hashed password.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ 
    Validates the provided password matching the hashed password 
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid 
