'''implementing queues using linked list
    TASK            TIME-COMPLEXITIES
  1) peek             O(1)
  2) enqueue          O(1)
  3) dequeue          O(1)

'''

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return(f"{self.value} -> {self.next}")


class Queue:

  def __init__(self):
  
    self.first = None
    self.last = None
    self.length = 0
    
  def peek(self):
  #check for length
    if self.length == 0:
      return None
    return self.first.value

  def enqueue(self, value):
    '''puts an element at the end of queue'''

    #create a new node and store the Value
    newNode = Node(value)

    #set first and last refereces
    #check for length
    if self.length == 0:
      self.first = newNode
      self.last= newNode
    else:
      #append in linked list
      self.last.next = newNode
      self.last = newNode
    
    #incement length of Queue
    self.length +=1

    return self.first
    
  def dequeue(self):
    #check for length
    if self.isEmpty():
      print("nobody in Queue")
      return

    #get the first element
    element = self.first.value

    #shift first pointer
    #holdigPointer = self.first
    self.first = self.first.next
    #decrement length of Queue
    self.length -=1
    
    return element

  def isEmpty(self):
    if self.length == 0:
      return True
    return False
  

myQ = Queue()
myQ.enqueue('Joy')
myQ.enqueue('Matt')
myQ.enqueue('Pavel')
print(myQ.peek())
print(myQ.dequeue())
print(myQ.enqueue('Samir'))
print(myQ.dequeue())
print(myQ.isEmpty())
print(myQ.dequeue())
print(myQ.isEmpty())
print(myQ.dequeue())
print(myQ.isEmpty())
print(myQ.dequeue())
print(myQ.isEmpty())

