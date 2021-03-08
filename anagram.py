# Function that determines if both strings provided are anagrams
def isAnagram(str1, str2):
  if str1 == '' or str2 == '':
    print('one of the strings is empty.')
    return False
  elif len(str1) != len(str2):
    print('these words are not the same length at least.')
    return False

  else:
    cache = {}

    for letter in str1:
      if letter not in cache:
        cache[letter] = 1
      else:
        cache[letter] += 1

    print('letters and their frequency of appearance: ', cache)
    for letter in str2:
      if letter not in cache:
        print('cache: ', cache)
        print('these words are not an anagram.')
        return False
      else:
        # because we know how many times the letters should appear in the 2nd word because of the 1st, we now subtract and bring the occurrances back to 0
        cache[letter] -= 1

    print('cache: ', cache)
    print('ayee, this is an anagram.')
    return True