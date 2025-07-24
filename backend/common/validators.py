def is_valid_email(email: str) -> bool:
    """
    Enforce that only tempohealthgroup.com emails register.
    """
    return email.lower().endswith('@tempohealthgroup.com')