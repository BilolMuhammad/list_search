def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    data = data
    data.sort()
    return data[0]


print(find_min([4, 2, 3, 2, 15, 1, 7]))
