def areThereDuplicates(*args):

    cache = {}
    for i in args:
        # Check for booleans since Python defaults them to 1s and 0s, which conflicts with those integers in cache
        if type(i) is bool:
            pass
        
        # Add values to cache to check when there is a duplicate
        elif i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1
            print(cache)
            print('Yes, there are duplicates.')
            return True

    print(cache)
    print('Nope, no duplicates here.')
    return False