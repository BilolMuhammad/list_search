def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    d = data
    d.sort()
    return data.count(d[0])


print(find_min_count([7, 6, 8, 41, 1, 1, 5, 1]))
