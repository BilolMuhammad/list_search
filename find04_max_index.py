def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    # i, _m = 0, 0
    # while i < len(data):
    #     if data[i] > _m:
    #         _m = data[i]
    #     i += 1
    # return data.index(_m)
    d = data
    d.sort()
    max = d[-1]
    return data.index(max)


print(find_max_index([2, 3, 1, 4, 7, 9]))
