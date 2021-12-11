def isNonBlankString(s: str):
    """
    A function to check a string is non-blank or not
    """
    return s is not None and isinstance(s, str) and len(s) > 0
