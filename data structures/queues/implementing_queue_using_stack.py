'''
implementing queue using 2 stacks as arrays
    TASK              TIME-COMPLEXITIE
    1) equeue             O(1)
    2) dequeue            O(n)
    3) peek               O(n)
    3) isEmpty            O(1)
'''

class Queue:
  def __init__(self):
    self.first = []
    self.second = []

  def enqueue(self, value):
    #put the element in first list
    self.first.append(value)

  def dequeue(self):

    if self.isEmpty() == True:
      return None

    #if second array is empty then first empty first array in second array such that last inserted element in first array is first inserted element in second array then pop from second array
    if len(self.second) == 0 :
      for _ in range(len(self.first)):
        self.second.append(self.first.pop())
    
    return self.second.pop()

  def peek(self):

    if self.isEmpty() == True:
      return None
    #if second array is empty then first empty first array in second array such that last inserted element in first array is first inserted element in second array then peek from second array

    if len(self.second) == 0:
      for _ in range(len(self.first)):
        self.second.append(self.first.pop())
    
    return self.second[len(self.second)-1]

  def isEmpty(self):
    if len(self.first) == 0 and len(self.second) ==0:
      return True
    else:
      False


myQueue = Queue()
print(myQueue.peek())
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.peek())

  

