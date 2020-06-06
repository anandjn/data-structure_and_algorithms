#!/bin/python
 '''implementing linked list 

    TASK          TIME-COMPLEXITY
  1.append            O(1)
  2.prepend           O(1)
  3.insert           *O(n)
  4.delete           *O(n)
  5.reverse           O(n)
  6.print             O(n)  '''

class LinkedList:
  #constuctor to initialise linked list with head and value
  def __init__(self, value):
    #creating head
    self.head = {'value' : value, 'next' : None}
    #tail is same as head as this is constructor
    self.tail = self.head
    self.length = 1
  
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
  
  def traverse(self, index):
    localHead = self.head
    for i in range(index):
        localHead = localHead['next']

    return localHead

  def insert(self, index, value):
    #if index is negative print error
    if index < 0:
      print("error: index is negative")
    #if index is more than length print error
    elif index >= self.length:
      print("error: out of bound")
    #if index == 0 then go for prepend
    elif index == 0:
      self.prepend(value)
    #if index == length of linked list then go for append
    elif index == self.length-1:
      self.appendIt(value)  
    #else create new node
    else:
      newNode = {'value': value, 'next': None}
      #break the list
      localHead = self.traverse(index-1)
      #append list[i to n] to new node
      newNode['next'] = localHead['next']
      #point the local head to newnode
      localHead['next'] = newNode
      #increment length of linked list
      self.length +=1 

  def delete(self, index):
    #check index
    if 0 > index or index > self.length-1:
      print("error: enter valid index") 
    else:
      #delete the indexed element and reduce length
      localHead = self.traverse(index-1)
      #make next of localHeadD to point to next of next node
      localHead['next'] = localHead['next']['next']
      self.length -= 1

  def reverse(self):
    #if length == 1 do nothing
    if(self.length == 1):
      return
    else:
      #grab first and second Node
      first = self.head
      second = first['next']

      #shift tail to head and head to tail
      self.head = self.tail
      self.tail = first 
      self.tail['next'] = None       
      
      #traverse till end and reverse link nodes
      while (second != None):
        temp = second['next']
        second['next'] = first
        first = second
        second = temp      
    
    return


  def printList(self):
    #iterate till none and return a list of values
    myarray = []
    currentNode = self.head
    while(currentNode):
      myarray.append(currentNode['value'])
      currentNode = currentNode['next']
    
    print(myarray)
    return myarray




mylist = LinkedList(10)
mylist.appendIt(55)
mylist.appendIt(16)
mylist.printList()
mylist.prepend(27)
mylist.printList()
mylist.insert(2, 200)
mylist.printList()
mylist.insert(3,100)
mylist.printList()
mylist.insert(4, 50)
mylist.printList()
mylist.insert(-2, 700)
print(mylist.traverse(1)['value'])
mylist.delete(4)
mylist.printList()
mylist.delete(6)
mylist.printList()
mylist.reverse()
mylist.printList()
