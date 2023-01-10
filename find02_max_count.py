def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    data = data
    data.sort(reverse=True)
    max1 = data[0]
    return data.count(max1)


print(find_max_count([1, 2, 1, 4, 3, 4, 4]))
