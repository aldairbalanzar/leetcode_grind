# Function that finds the first pair that sums to 0
def sumZero(arr):
  if len(arr) <= 1:
    print('please provide an array with at least two sorted values.')
    return False
  else:

    left = 0
    right = len(arr) - 1
    sumAnswer = None

    while left != right:
      sumAnswer = arr[left] + arr[right]

      if sumAnswer > 0:
        right -= 1
      elif sumAnswer <  0:
        left += 1
      else:
        return [arr[left], arr[right]]
    
    print('nothing sums to 0.')
    return False