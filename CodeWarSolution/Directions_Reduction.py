# Directions Reduction
# Cancel opposite directions if they appear side by side (e.g. W<->E, N<->S)

def dirReduc(arr):
    opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "WEST":"EAST", "EAST":"WEST"}
    result = []
    for i in arr:
        if result and opposite[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result
