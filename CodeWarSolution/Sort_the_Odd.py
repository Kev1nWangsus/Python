# Sort the odd
# Given a list of integers, sort all the odds

def sort_array(source_array):
    odds = []
    for i in source_array:
        if i % 2 == 1:
            odds.append(i)
    odds.sort()
    for e in source_array:
        if e % 2 == 0:
            odds.insert(source_array.index(e), e)
    return odds
