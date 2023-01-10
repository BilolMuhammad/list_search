def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    data = data
    data.sort()
    return data.index(data[-1])


print(find_max_index([2, 3, 1, 4, 7, 9]))
