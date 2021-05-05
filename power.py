# Returns power of base to the exponent
def power(base, exp):
    # case that breaks recursion
    if exp == 0:
        return 1
    else:
       return base * power(base, exp - 1)