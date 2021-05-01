# finds max sum of subarray that is determined by given size
def maxSubArraySum(arr, num):
  if num > len(arr):
    print('array is too small for chosen sub array size.')
    return False

  else:
    maxSum = 0
    currSum = 0
    for i in range(num):
      maxSum += arr[i]
    
    # subtracts first value from last sum, then adds next incoming value as window slides
    currSum = maxSum
    for i in range(num, len(arr)):
      currSum = currSum - arr[i - num] + arr[i]
      if currSum > maxSum:
        maxSum = currSum

    return maxSum