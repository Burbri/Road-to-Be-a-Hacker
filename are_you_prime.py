import math


def are_you_prime(x):
    n = math.floor(math.sqrt(x))
    for i in range(n):
        if x % (i+2) == 0:
            return False
    return True
            
