# iterates through string to find match of second string provided within first string
def naiveSearch(string, match):
    p1 = 0
    for i, char in enumerate(string):
        # resets char pointer if chars from both strings do not match
        if char != match[p1]:
            print(f'{char}-{match[p1]} no match')
            p1 = 0

        # increments char pointer for match to be found
        if char == match[p1]:
            print(f'{char}-{match[p1]} char match')
            p1 += 1
        
        if p1 == len(match):
            print(f'{match} found within string.')
            return

    print('match not found within string.')
    return