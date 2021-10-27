def remove_null_values(lst: list):
    i = 0
    while 0 in lst:
        lst.remove(0)
    i += 1
    return lst


