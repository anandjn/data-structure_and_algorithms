#!/usr/bin/python3
'''implementing doubly linked list 

    TASK          TIME-COMPLEXITY
  1.append            O(1)
  2.prepend           O(1)
  3.insert           *O(n)
  4.delete           *O(n)
  5.print             O(n)  '''

class DoublyLL:
  
  #initialise DLL
  def __init__(self, value):
    #create Head
    self.head = {
      'value' : value,
      'next' : None,
      'previous' : None
    }
    #create tail
    self.tail = self.head
    #create length
    self.length = 1

    #print(self.head)

  def append (self, value):
    '''add new node to end'''
    #create new node
    newNode = {
      'value' : value,
      'next' : None,
      'previous' : None
    }
    #go to tail and cross reference
    newNode['previous'] = self.tail
    self.tail['next'] = newNode
    
    #modify tail and length
    self.tail = self.tail['next']
    self.length += 1

    #print(self.head)

  def prepend (self, value):
    '''add a node at starting'''
    #create new node
    newNode = {
      'value' : value,
      'next' : None,
      'previous' : None
    }

    #modify head and length
    newNode['next'] = self.head
    self.head['previous'] = newNode
    self.head = newNode
    self.length += 1

    #print(self.head)
  def insert(self, index, value):
    '''add a node at specefic index'''
    #check for valid index
    if index >= self.length or index < 0:
      print("error: out of bound")
      return None
    elif index == 0:
      self.prepend(value)
    elif index == self.length-1:
      self.append(value)
    else:
      #create new node
      newNode = {
        'value' : value,
        'next' : None,
        'previous' : None
      }
      #grab the reference to index-1th node and ith node
      leader = self.traverse(index-1)
      follower = leader['next']
      
      newNode['previous'] = leader
      newNode['next'] = follower

      leader['next'] = newNode
      follower['previous'] = newNode

      #increment length
      self.length += 1
      print(self.head)

  def delete(self, index):
    '''remove a node at specefic index'''
    #check for valid index
    if index >= self.length or index < 0:
      print("error: out of bound")
      return None
    else:
      #grab index-ith and index+ith node
      leader = self.traverse(index-1)
      follower = leader['next']
      nextFollower = follower['next']
      
      leader['next'] = nextFollower
      nextFollower['previous'] = leader

      #reduce length
      self.length -= 1



  def traverse(self, index):
    currentNode = self.head
    for _ in range(index):
      currentNode = currentNode['next']
    return currentNode

  def printDLL(self):
    DLL = []
    currentNode = self.head
    while(currentNode != None):
      DLL.append(currentNode['value'])
      currentNode = currentNode['next']
    
    print(DLL)
    return DLL

#
myDLL = DoublyLL(1)
myDLL.append(2)
myDLL.prepend(0)
myDLL.insert(1, 20)
myDLL.printDLL()
myDLL.delete(2)
myDLL.printDLL()
