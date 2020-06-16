'''implementing recursion for factorial
    TASK              TIME-COMPLEXITY
  1) factorial-Loop       O(n)
  2) factorial-recursion  O(n)
  '''

def factorialByLoop(number):
  answer = 1
  for num in range(2, number+1):
    answer = answer*num
  return answer

def factorialByRecursion(number):
  if number == 1 :
    return 1
  return (number) * factorialByRecursion(number-1)

print(factorialByLoop(2))
print(factorialByRecursion(5))
