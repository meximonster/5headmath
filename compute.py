import constants
import math

def compute_upper(ar,su,sl,slr):
    return round(ar - su - 2*constants.Uupper[slr], 1)

def compute_lower(ar,sl,slr):
    return round(ar - sl - 2*constants.Ulower[slr], 1)

def switch(s):
    if len(str(s).split('.')[1]) <= 2:
        format(s, '.2f')
    else:
        s = round(s, 2)
    num = float(str(s).split('.')[0])
    dec = float(str(s).split('.')[1])
    if 0 <= dec < 25:
        return num
    elif 25 <= dec < 75:
        return float(str(s).split('.')[0]+".5")
    else:
        return num+1