''' implementing selection sort
        TASK              TIME-COMPLEXITY
  1) selection_sort           O(n**2)
'''

def selectionSort(array):

  for i in range(len(array) -1):
    minima_index = i   
    for j in range(i, len(array)-1): 
      if array[i] > array[j+1]:
        minima_index = j+1
    #by the end of above loop I'll have minimum value and its index
    #replace it with i-th index
    print(array)
    temp = array[i]
    array[i] = array[minima_index]
    array[minima_index] = temp
    
    #repeat the above loop len(array) times and change initial position each time
  return array

print(selectionSort([5,4,3,2,1,44,40,32,56,4433]))
