'''implementing bubble sort
      TASK              TIME-COMPLEXITY
  1) bubbleSort          O(n**2) '''



def bubbleSort(array):
  #repeat below steps until there seems no change
  for _ in range(len(array)):
    #keep swapping
    for i in range(len(array)-1):
      #if first number is greater than second then swap them
      if array[i] > array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
  return(array)


print(bubbleSort([10,12,23,40,55,2,4,5,6]))
    

