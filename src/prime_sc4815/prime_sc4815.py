import math

def is_prime(n):
    """
    check if a given integer is a prime number

    Integer
    -------
    n
    
    Returns
    -------
    'True' if the input integer (n) is prime
    'False' otherwise.
    
    Examples
    --------
        >>> is_prime(13)
        True
        >>> is_prime(6)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True