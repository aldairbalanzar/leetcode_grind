#Determines if pair of integers have the same numbers and frequencies
def sameFrequency(num1, num2):
    # Turn Ints into type Strings for iterating ability
    num1 = str(num1)
    num2 = str(num2)

    if len(num1) != len(num2):
        print('One of the numbers is bigger in length than the other.')
        return False
    else:
    # Init cache to store numbers and their frequencies
        cache = {}

        # Iterate through 1st integer and increment cache values by 1 according to occurrance.
        for num in num1:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

        # Iterate through 2nd integer and decrease cache values by 1 according to occurrance. If iteration value is not in cache, return False because integers are different
        for num in num2:
            if num not in cache:
                print('These integers have different digits.')
                return False
            else:
                cache[num] -= 1
        
        # Make sure that cache values all have 0 as value as indicator that they appear at same frequency in both integers
        for num in cache:
            if cache[num] != 0:
                print('These integers do not have numbers that repeat at same frequency.')
                return False

    print(f"Cache: {cache}")
    return True