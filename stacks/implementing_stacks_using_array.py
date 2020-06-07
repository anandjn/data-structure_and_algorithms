#!/bin/python

'''implementing stacks using arrays
    TASK                TIME COMPLEXITY
  1. Peek                     O(1)
  2. Push                     O(1)
  3. Pop                      O(1)
  4. IsEmpty                  O(1)
'''



class Stack:
  '''creates stack using list'''

  def __init__(self):
    '''initializes new stack'''
    self.stack = []
    self.length = len(self.stack)

  def peek(self):
    '''return top most value of stack'''
    if len(self.stack) == 0:
      return None
    return self.stack[len(self.stack)-1]

  def push(self, value):
    '''push value in stack /i list we will append'''
    self.stack.append(value)
    return self.stack

  def pop(self):
    '''pops value from stack/ in  list we will use predefied pop method'''
    #check length before popping
    if len(self.stack) == 0:
      return None
    popped = self.stack.pop()   

    return popped

  def isEmpty(self):
    if len(self.stack) == 0:
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





