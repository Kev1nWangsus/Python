#Stock List

def stock_list(listOfArt, listOfCat):
    plist = []
    for i in listOfArt:
        plist.append(i.split())
    listheap = []
    for letter in listOfCat:
        sumheap = 0
        
        for item in plist:
            if item[0][0] == letter:
                sumheap += int(item[1])
                
        if plist:
            listheap.append("({} : {})".format(letter, sumheap))
    return " - ".join(listheap)
                
                
