def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max = data
    max.sort(reverse=True)
    return max[0]


print(find_max([2, 1, 4, 9, 7]))
