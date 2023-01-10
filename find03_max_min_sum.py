def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    data = data
    data.sort()
    return data[0]+data[-1]


print(find_max_min_sum([3, 2, 3, 4, 9]))
