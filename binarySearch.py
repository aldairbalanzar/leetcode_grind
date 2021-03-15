# searches a sorted array for gieven target using a divide & conquer method
# returns index
def binarySearch(arr, target):
  if len(arr) < 1:
    print('please provide an array with at least one value')

  else:
    min = 0
    max = len(arr) - 1
    while min <= max:
      mid = (min + max) // 2

      if arr[mid] < target:
        min = mid + 1
      elif arr[mid] > target:
        max = mid - 1
      else:
        return mid
        
    print('that number does not exist in given array.')
    return False