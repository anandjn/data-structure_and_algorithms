'''implementing mergesort
    TASK                  TIME-COMPLEXITY
  1) mergeSort                 O(nlogn)'''

def mergeSort(array):
  #we will use recursion here
  
  length = len(array)
  #base case
  if length == 1:
    return array
  
  #divide the array
  leftArray = array[: length//2]
  rightArray = array[length//2: ]

  #merge the sorted array and return
  #print("divide")
  return(merge(mergeSort(leftArray), mergeSort(rightArray)))

#merging function
def merge(left, right):
  tempArray = []
  length_of_left = len(left)
  length_of_right = len(right)
  print(left, right)

  l = 0
  r = 0
  #start merging and exhaust any of left or right array first
  while l < length_of_left and r < length_of_right:
    #if any array exhaust then break
    #print(length_of_left, length_of_right)
    if (left[l] <= right [r]) :
      tempArray.append(left[l])
      l +=1
    else:
      tempArray.append(right[r]) 
      r +=1
  
  #merge the unexhausted array
  if(l < length_of_left):
    #merge the remaing left array
    tempArray.extend(left[l:])
  elif(r < length_of_right):
    #merge the remaining right array
    tempArray.extend(right[r:])

  return tempArray

mylist = [2,0,6,9,7,4,6,5,8,45,6879,84,65]
print(mergeSort(mylist))
