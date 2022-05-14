# Function that finds the amount unique values in array.
def uniqueValuesCounter(arr):
  if len(arr) < 1:
    print('This array is empty.')

  pointer1 = 0
  pointer2 = 1
  counter = 1
  while pointer2 <= len(arr) - 1:
    if arr[pointer1] != arr[pointer2]:
      print('unique value')
      counter += 1
      pointer1 += 1
      pointer2 += 1
    else:
      pointer1 += 1
      pointer2 += 1
  
  return counter