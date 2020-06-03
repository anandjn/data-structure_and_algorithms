#!/bin/python
'''implementing linked list '''

class LinkedList:
  #constuctor to initialise linked list with head and value
  def __init__(self, value):
    #creating head
    self.head = {'value' : value, 'next' : None}
    #tail is same as head as this is constructor
    self.tail = self.head
    self.length = 1
    self.data = value
  
  def appendIt(self , value):
    '''append a new node to exixting linked list at last postion'''
    #create node
    newNode = {'value' : value, 'next' : None}
    #go to tail and append Value
    self.tail['next'] = newNode
    #get new tail
    self.tail = newNode
    #increment length
    self.length += 1

  def prepend(self, value):
    ''' add a node at begining'''
    #create new node
    newNode = {'value' : value, 'next' : None}
    #modify new node to point to head
    newNode['next'] = self.head
    #modify old head point new node
    self.head = newNode
    #increment length
    self.length +=1

  def insert(self, index, value):
    #if index == 0 then go for prepend
    if index == 0:
      self.prepend(value)
    #if index == length of linked list then go for append
    elif index == self.length-1:
      self.appendIt(value)
    #if index is negative print error
    elif index < 0:
      print("error: index is negative")
    #if index is more than length print error
    elif index >= self.length:
      print("error: out of bound")  
    #else create new node
    else:
      newNode = {'value': value, 'next': None}
      #break the list
      self.localHead = self.head
      #loop until we point at (i-1)th index
      for i in range(index-1):
        self.localHead = self.localHead['next']
      #now local head is pointing to (i-1)th index
      #append list[i to n] to new node
      newNode['next'] = self.localHead['next']
      #point the local head to newnode
      self.localHead['next'] = newNode 

  def printList(self):
    #iterate till none and return a list of values
    self.myarray = []
    self.currentNode = self.head
    while(self.currentNode):
      self.myarray.append(self.currentNode['value'])
      self.currentNode = self.currentNode['next']
    
    print(self.myarray)
    return self.myarray




mylist = LinkedList(10)
mylist.appendIt(55)
mylist.appendIt(16)
mylist.printList()
mylist.prepend(27)
mylist.printList()
mylist.insert(3, 100)
mylist.printList()
mylist.insert(6, 100)
mylist.printList()
mylist.insert(-2, 100)




