'''implementing fibonacci sequence using recursion
    TASK                      TIME-COMPLEXITY
  1) numberAtIndex_Loop             O(n)
  1) numberAtIndex_Recursion        O(2**n)

  Fibonacci Sequence : 0 1 1 2 3 5 8 13 21 34 55
  '''

def numberAtIndex_Loop(index):
  # returns the number present at index position of fibonacci sequence using loop statement
  first = 0
  second = 1
  if index == 0:
    return first

  if index == 1:
    return second

  answer = 0

  for number in range(index-1):
    answer = first + second
    first = second
    second = answer
  return answer

def numberAtIndex_Recursion(index):
  if index == 0:
    return 0
  if index == 1:
    return 1

  return numberAtIndex_Recursion(index -1) + numberAtIndex_Recursion(index -2)

print(numberAtIndex_Loop(40))
print(numberAtIndex_Recursion(40))


