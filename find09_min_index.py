def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i, min = 0, data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i += 1
    return data.index(min)


print(find_min_index([3, 5, 2, 1]))
