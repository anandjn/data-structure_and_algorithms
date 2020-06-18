'''implementing insertion sorted
      TASK              TIME-COMPLEXITY
  1) insertionSort          O(n**2) '''

def insertionSort(array):
  #for all elements
  for i in range(1, len(array)):
    key = array[i]
    #for all elements behind i
    j = i-1
    #make space by shifting elements 1 cell ahead which are greater than key
    while j >=0 and array[j] > key:
      array[j+1] = array[j]
      j -= 1
    #place our key at new j+1th position
    array[j+1] = key   

  return array

print(insertionSort([1,2,3,4,5,100,7,8,9,10]))

