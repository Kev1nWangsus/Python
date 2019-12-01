# Dec2Fac_Fac2Dec

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def find1st(nb):
    for i in range(36, -1, -1):
        if nb // factorial(i):
            return i

def dec2FactString(nb):
    idx = find1st(nb)
    res = ""
    while idx >= 0:
        if idx >= 10:
            if nb // factorial(idx) >= 10:
                res += chr(nb // factorial(idx) + 55)
            else:
                res += str(nb // factorial(idx))
            nb = nb % factorial(idx)
            idx -= 1
        else:
            res += str(nb // factorial(idx))
            nb = nb % factorial(idx)
            idx -= 1
    return res

def factString2Dec(string):
    s = list(reversed(string))
    num = 0
    for i in range(0, len(s)):
        if ord(s[i]) >= 65:
            num += (ord(s[i]) - 55) * factorial(i)
        else:    
            num += int(s[i]) * factorial(i)
    return num
