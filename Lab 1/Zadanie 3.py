list = [3, -2, 45, -214, -432, 5, 9]
def ile_ujemnych(list):
    ujemne = 0
    for x in list:
        if x < 0:
            ujemne += 1
    return ujemne


print(ile_ujemnych(list))
