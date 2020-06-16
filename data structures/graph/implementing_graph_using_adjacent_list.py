'''implementing graphs using adjacent list
    TASK                TIME-COMPLEXITY
1. adding a vertex        O(1)
2. adding an edge        O(1)
3. show all connection    O(n**2) '''

class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacentList = {}

  def addVertex(self, node) :
    #add that specific key to list
    self.adjacentList[node] = []
    #increment number of nodes
    self.numberOfNodes += 1

  def addEdge(self, node1, node2):
    #add node2 at key = node1 in adjacent list and vice versa
    #assuming node1 and node2 exist as keys in adjacent list
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)

  def showConnection(self):
    #prints connections of each node
    nodes = self.adjacentList.keys()
    for node in nodes:
      connection = str(node) + " -->"
      connectingNodes = self.adjacentList[node]
      for connectingNode in connectingNodes:
        connection = connection + ", " + str(connectingNode)
      print(connection)
    return 


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
myGraph.showConnection()


