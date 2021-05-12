def recursiveRange(num):
    if num == 1:
        return 1
    else:
        # Decrements num passed to function until break point is reached
        return num + recursiveRange(num - 1)