import constants
import math

def compute_upper(ar,su,sl):
    return round(ar - su - 2*constants.Uupper[sl], 1)

def compute_lower(ar,sl):
    return round(ar - sl - 2*constants.Ulower[sl], 1)