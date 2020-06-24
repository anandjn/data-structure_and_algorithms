'''implementing breadth first search
        TASK               TIME-COMPLEXITY
  1)  breadthFirstSearch    O(n) 
  2)  depthFirstSearch      O(n)'''

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
    #travel tree to find given element and return it if found else return None
    currentNode = self.root
    while True:
      if currentNode == None:
        return None
      elif value == currentNode.value:
        return currentNode.value
      elif value > currentNode.value:
        #move right
        currentNode = currentNode.right
      elif value < currentNode.value:
        #move left
        currentNode = currentNode.left

  
  def remove(self, value):
    '''1) if the node is leaf remove it directly
    2) if node has only one child then child takes parent's place 
    3) if there exist a sub-tree then left most node(that node may have 0 or 1 child) takes that position'''
    #check if the node exist in tree
    if self.lookup(value) == None:
      print("wrong value")
      return None
    else:
      #find that Node
      currentNode = self.root
      parentHoldingNode = None
      holdingNode = None
      while True:
        if value == currentNode.value:
          holdingNode = currentNode
          break
        elif value > currentNode.value:
          #go right
          parentHoldingNode = currentNode
          currentNode = currentNode.right
        elif value < currentNode.value:
          #go left
          parentHoldingNode = currentNode
          currentNode = currentNode.left

      ########################   LEAF    #######################
      #if holding node is leaf node then remove it with help of parent holding Node
      if holdingNode.left == None and holdingNode.right == None:
        #it is a leaf Node
        #make its parent branch which pointing to value to point to None and return
        if parentHoldingNode.left.value == value:
          parentHoldingNode.left = None
          #returning value which we have removed
          return value
        else:
          parentHoldingNode.right = None
          #returning value which we have removed
          return value
      ########################   1 CHILD     #######################
      #if holding node has 1 child then make child to take place of holding Node
      elif holdingNode.left == None or holdingNode.right == None:
        #check which side of holding node has child then make parent to point that child
  
        if holdingNode.left != None:
          #holdingNode has left child
          #parent to left child of holding pointer
          if parentHoldingNode.left.value == value:
            parentHoldingNode.left = holdingNode.left
            return value
          else:
            parentHoldingNode.right = holdingNode.left
            return value
        else:
          #holdingNode has right child
          if parentHoldingNode.left.value == value:
            parentHoldingNode.left = holdingNode.right
            return value
          else:
            parentHoldingNode.right = holdingNode.right
            return value
      
      ########################   2 CHILD     #######################
      #if holding node has 2 Child, go to succesor
      #____________ RIGHT CHILD IS LEAF_____________#
      if holdingNode.right.left == None and holdingNode.right.right == None:
        #join parent of holding to child of holding
        if parentHoldingNode.left.value == value:
          #parent's left branch
          currentNode.right.left = currentNode.left
          parentHoldingNode.left = holdingNode.right
          return value
        else:
          #parent's right branch
          holdingNode.right.left = holdingNode.left
          parentHoldingNode.right = holdingNode.right
          return value

      #____________ RIGHT CHILD IS SUBTREE_____________#
      #go to left most of this sub tree(smallest value) and replace

      else:
        subHolding = holdingNode.right
        subHoldingParent = holdingNode
        while True:
          #if subHolding is the left most then join and return else traverse
          if subHolding.left == None:
            subHoldingParent.left = subHolding.right
            subHolding.left = holdingNode.left
            subHolding.right = holdingNode.right
            
            parentHoldingNode.right = subHolding
            return value
          else:
            subHoldingParent = subHolding
            subHolding = subHolding.left
            
  def breadthFirstSearch(self):
    currentNode = self.root
    answer = []
    queue = []
    queue.append(currentNode)
    while(len(queue) != 0):
      currentNode = queue.pop(0)
      answer.append(currentNode.value)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    return answer

  def breadthFirstSearchR(self, queue, mylist):
    if(len(queue) == 0):
      return mylist
    currentNode = queue.pop(0)
    mylist.append(currentNode.value)
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)
    
    return self.breadthFirstSearchR(queue, mylist)

  def DFS_inorder(self):
    return  traverseInorder(self.root, [])

  def DFS_preorder(self):
    return  traversePreorder(self.root, [])

  def DFS_postorder(self):
    return  traversePostorder(self.root, []) 

def traverseInorder(node, mylist):
  #print(node.value)
  if node.left:
    traverseInorder(node.left, mylist)

  mylist.append(node.value)
  
  if node.right:
    traverseInorder(node.right, mylist)

  return mylist


def traversePreorder(node, mylist):
  mylist.append(node.value)
  if node.left :
    traversePreorder(node.left, mylist)

  if node.right :
    traversePreorder(node.right, mylist)

  return mylist  

def traversePostorder(node, mylist):
  if node.left:
    traversePostorder(node.left, mylist)

  if node.right:
    traversePostorder(node.right, mylist)

  mylist.append(node.value)
  
  return mylist

'''
     10
   /    \
  5     20
 / \    / \
1   8  15  40

BFS = [10, 5, 20, 1, 8, 15, 40]
DFS
  inorder = [1, 5, 8, 10, 15, 20, 40]
  preorder = [10, 5, 1, 8, 20, 15, 40 ]
  postorder = [1, 8, 5, 15, 40, 20, 10]
'''      


myTree = BinarySearchTree()
myTree.insert(10)
myTree.insert(5)
myTree.insert(20)
myTree.insert(1)
myTree.insert(8)
myTree.insert(15)
myTree.insert(40)
print("BFS-iterative: ")
print(myTree.breadthFirstSearch())
print("BFS-recursive")
print(myTree.breadthFirstSearchR([myTree.root], []))
print("DFS")
print("Inorder")
print(myTree.DFS_inorder())
print("Preorder")
print(myTree.DFS_preorder())
print("Postorder")
print(myTree.DFS_postorder())




