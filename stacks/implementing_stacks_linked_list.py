#!/bin/python

'''implementing stacks using linked list  top(1) --> (2) --> (3)(bottom)
    TASK                TIME COMPLEXITY
  1. Peek                     O(1)
  2. Push                     O(1)
  3. Pop                      O(1)
  4. IsEmpty                  O(1)
'''



class Node:
  '''creates bode objects''' 
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return(f"{self.value} -> {self.next}")

class Stack:
  '''creates stack using linked list'''

  def __init__(self):
    '''initializes new stack'''
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    '''return top most value of stack'''
    return self.top.value

  def push(self, value):
    '''push value in stack / in linked list we will prepend'''

    #create a Node and put value in it
    newNode = Node(value)
    #check if length is 0
    if self.length == 0:
      #point bottom
      self.bottom = newNode
    #make new node to point old top and modify top to new node
    newNode.next = self.top
    self.top = newNode
    #increment length
    self.length +=1
    return self.top

  def pop(self):
    '''pops value from stack/ in linked list we will shoft head'''
    #check length before popping
    if self.length == 0:
      self.bottom = None
      return None
    popped = self.top.value
    #shift head pointer of linked list
    self.top = self.top.next    
    #decrement length
    self.length -=1
    return popped

  def isEmpty(self):
    if self.length == 0:
      return True
    return False


myStack = Stack()

myStack.push('google')
myStack.push('udemy')
print(myStack.push('Disord'))

print(myStack.peek())
print('here i pop')
print(myStack.pop())
print(myStack.isEmpty())
print('here i pop')
print(myStack.pop())
print(myStack.isEmpty())
print('here i pop')
print(myStack.pop())

print(myStack.isEmpty())
print('here i pop')
print(myStack.pop())

print(myStack.isEmpty())
print('here i pop')
print(myStack.pop())





