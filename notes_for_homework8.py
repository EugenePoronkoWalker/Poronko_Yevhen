def sum_numbers(first, second):
    """
    Function summarizes two numbers
    Args:
        first (integer or float): number
        second (integer or float): number
    Returns:
        integer : number (sum of first and second numbers)
    """
    return first + second

def find_substring(str1, str2):
    """
    Function that takes two strings and returns the index of the first
    occurrence of the second string in the first string
    Args:
        str1 (string): first line
        str2 (string): second line

    Returns:
        integer : index
    """
    index = str1.find(str2)
    return index
