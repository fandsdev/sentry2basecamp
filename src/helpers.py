def str_to_bool(val: str) -> bool:
    """
    Convert a string representation of truth to true (1) or false (0).

    distutils.strtobool is deprecated in python 3.10.

    >>> str_to_bool('true')
    True
    >>> str_to_bool('On')
    True
    >>> str_to_bool('1')
    True

    >>> str_to_bool('false')
    False
    >>> str_to_bool('Off')
    False
    >>> str_to_bool('0')
    False
    >>> str_to_bool('xyz')
    Traceback (most recent call last):
        ...
    ValueError: invalid truth value 'xyz'

    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))
