def mult(*arg):
    iloczyn = 1
    for x in arg:
        iloczyn *= x
    return iloczyn

print(mult(3, 5, 7))