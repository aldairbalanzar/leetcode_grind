# Returns the product of values in given list
def productOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        # Passes list with last element sliced off when function is called
        return arr[len(arr) - 1] * productOfArray(arr[0:len(arr) - 1])