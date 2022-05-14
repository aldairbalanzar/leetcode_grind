# function that reverses string passed into arguments
def reverseString(string):
    # makes sure type is of str
    if type(string) is not str:
        print('argument should be of type string.')
        return

    # makes sure there are chars in string
    if len(string) < 1:
        print('string argument needs to contain at least 1 character.')
        return

    # iterate through string starting from end and adding each char to reversedString
    end = len(string) - 1
    reversedString = ''
    while end >= 0:
        reversedString += string[end]
        end -= 1

    print(reversedString)
    return