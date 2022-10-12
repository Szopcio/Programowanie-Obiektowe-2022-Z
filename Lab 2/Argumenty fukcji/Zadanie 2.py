def mult_ints(*arg):
    iloczyn = 1
    for x in arg:
        if type(x) == int:
            iloczyn *= x
    return iloczyn


print(mult_ints(3, 3.14, 5, "abc", 7))
