def fibonacci(num):
    # Automatically return 1 if the argument is equal or less than 2 because first two numbers in sequence are 1
    if num <= 2:
        return 1
    else:
        # Keep subtracting from argument until break case can be reached
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(4))