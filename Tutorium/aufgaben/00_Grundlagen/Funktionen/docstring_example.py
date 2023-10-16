def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The sum of the numbers.

    Raises
    ------
    TypeError
        If the input is not a list.
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> calculate_sum([1, 2, 3, 4, 5])
    15.0
    >>> calculate_sum([])
    Traceback (most recent call last):
        ...
    ValueError: Input list is empty.

    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("Input list is empty.")
    
    return sum(numbers)
