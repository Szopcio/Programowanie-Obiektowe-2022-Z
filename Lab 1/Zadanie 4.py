list = [1, 2, 4, -2, 5]

def iloczyn(list):
    iloczyn = 1
    for x in list:
            iloczyn *= x
    return iloczyn


print(iloczyn(list))
