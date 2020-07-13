'''using dynamic programming to calculate n-th fibonacci number
      TASK                TIME COMPLEXITY
    1) fibonacci                O(2**n)
    2) fibonacciDP              O(n)'''



calculations = 0

#slow version
def fibonacci(n):
  global calculations
  calculations = calculations + 1
  
  if n < 2 :
    return n
  return fibonacci(n-1)+ fibonacci(n-2)

#fast version
def fibonacciDP():
  cache = {}

  def fibonacci(n):
    global calculations
    calculations = calculations + 1
    if n in cache :
      return cache[n]
    else:
      if n < 2 :
        return n

      cache[n] = fibonacci(n-1)+ fibonacci(n-2)
      #print(cache)
      return cache[n]

  return fibonacci

fibonacci_calculator = fibonacciDP()
print(fibonacci_calculator(10))
print ("calculation : " + str(calculations))
