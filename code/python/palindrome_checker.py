def is_palindrome(value: int) -> bool:
    """
    Check whether a given integer is a palindrome.

    A palindrome number reads the same forwards and backwards.
    Examples: 121, 1331.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    if value < 0:
        return False

    original = value
    reverse = 0

    while value > 0:
        digit = value % 10
        reverse = reverse * 10 + digit
        value //= 10

    return original == reverse
