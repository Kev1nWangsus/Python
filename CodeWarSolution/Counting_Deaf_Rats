# Counting deaf rats

def count_deaf_rats(town):
    lst = town.split("P")
    deafrat = 0
    count = 0
    for i in range(0, len(lst[0])):
        if lst[0][i] == "~":
            count += 1
            i += 1
        elif lst[0][i] == "O":
            count -= 1
            if count < 0:
                deafrat += 1
    count = 0
    for i in range(0, len(lst[1])):
        if lst[1][i] == "O":
            count += 1
        elif lst[1][i] == "~":
            count -= 1
            if count < 0:
                deafrat += 1
    return deafrat
