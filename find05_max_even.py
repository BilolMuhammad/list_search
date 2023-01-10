def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    data = data
    data.sort()
    i = 0
    ans = 0

    while i < len(data):
        if data[i] % 2 == 0:
            ans = data[i]

        i += 1
    if ans == 0:
        return -1
    return ans


print(find_max_even([1,  3, 1, 29]))
