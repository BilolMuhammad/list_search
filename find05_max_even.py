def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    data = data
    data.sort()
    idx = 0
    ans = []
    con = 0

    while con < len(data):
        if data[idx] % 2 == 0:
            ans.append(data[idx])
        idx += 1
        con += 1
    return ans


print(find_max_even([1, 2, 3, 1, 29, 6, 0]))
