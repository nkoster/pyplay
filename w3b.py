import math
import sys

alpha = "dn6ksvwg8aqht5jmzl7crxe4y9ip2b3o10uf"

def numToAlpha(num):
    r = ""
    n = int(math.floor(int(num) / len(alpha)))
    if n > 0:
        r += numToAlpha(n)
    r += alpha[int(num) % len(alpha)]
    return r

def alphaToNum(s):
    r = 0
    i = len(s)
    s = s[::-1]
    while i >= 0:
        i -= 1
        r += alpha.find(s[i]) * pow(len(alpha), i)
    return int(r)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if isInt(arg):
        print('string = %s' % numToAlpha(arg))
    else:
        print('number = %s' % alphaToNum(arg))
