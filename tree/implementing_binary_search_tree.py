'''implementing binary search tree
    TASK            TIME-COMPLEXITY
  1) insert             O(logn)
  2) LookupError        O()
  3) remove             O() '''

class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return(f"(value: {self.value} \n left : {self.left} \t right: {self.right})")

class BinarySearchTree:

  def __init__(self):
    self.root = None

  #check if it is root node
  def insert(self, value):
    
    #create a Node
    newNode = Node(value)
    
    if(self.root == None):
      self.root = newNode
      return self.root
    else:
      currentNode = self.root
      #follow instruction to append it to right place
      while True:
        if currentNode == None:
          currentNode = newNode
          return self.root
        else:
          if currentNode.value < value:
            #move right
            if(currentNode.right == None):
              currentNode.right = newNode
              return self.root
            currentNode = currentNode.right

          else: 
            #move left
            if(currentNode.left == None):
              currentNode.left = newNode
              return self.root
            currentNode = currentNode.left


  def lookup(self, value):
    pass

  
  def remove(self, value):
    pass


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
print(myTree.insert(1))



