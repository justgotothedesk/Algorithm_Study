import math

def solution(numer1, denom1, numer2, denom2):
    denomGcd = math.gcd(denom1, denom2)
    multiple1 = denom2 // denomGcd
    multiple2 = denom1 // denomGcd
    denom = denom1 * multiple1
    numer = (numer1 * multiple1) + (numer2 * multiple2)
    
    finalGcd = math.gcd(denom, numer)
    return [numer // finalGcd, denom // finalGcd]
