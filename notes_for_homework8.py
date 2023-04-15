def sum_numbers(first, second):
    """
    This function summarizes two numbers
    Args:
        first (integer or float): number
        second (integer or float): number
    Returns:
        integer : number (sum of first and second numbers)
    """
    return first + second


def arithmetic_average(list_numbers):
    """
    This function counts the arithmetic mean of a list of numbers
    Args:
        list_numbers (list): list of numbers
    Returns:
        integer : number
    """
    return int(sum(list_numbers) / len(list_numbers))
