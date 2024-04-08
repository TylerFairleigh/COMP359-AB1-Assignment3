import networkx as netx
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation as anim
import random as rand

# You can declare the maximum number of possible nodes here
maxNodes = 20

# Class for Union-Find. This version uses both path compression and union by size.
class UnionFind:
    def __init__(self, n):
        self.parent = [1] * n # Create an array for parents which is the size n - 1
        self.size = [1] * n # Size array must be same size as parent array (used for union by size)
        self.graph = netx.Graph() # Declare NetworkX graph such that it can be
        self.steps = [] # This keeps track of the steps for which the plot will display on each iteration of the algorithm for visualization purposes

    # implementation of Find with Path Compression
    def find(self, node):
        # Base-case, check if current node is a root (ie. its own parent)
        if (self.parent[node] == node):
            return node
        else:
            # Recursively call find function until a valid parent is found
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

    # implementation of Union By Size
    # This makes the node with more children the parent when attempting to joint two nodes
    def union(self, p, q):
        # This ensures that the graph before the unions occur is copied such that it can be displayed
        if len(self.steps) == 0:
            self.steps.append(self.graph.copy())  # Store current step for visualization purposes
        r = self.find(p)
        s = self.find(q)

        if (r == s):
            self.parent[r] = s
            self.parent[s] = r
            return
        if (self.size[r] < self.size[s]): # if the size of node s is bigger than node r, set node s as node r's parent
            self.parent[r] = s
            self.size[s] += self.size[r] # update the size of the node (ie. add the sizes of both nodes r and s together)
        else:
            self.parent[s] = r # similar to the if-statement, nodes are simply swapped here (r becomes parent of s)
            self.size[r] += self.size[s] # once again, update size now that the nodes have been joined
        #print("Joined " + str(r) + " with " + str(s))
        # This is solely used for visualiztion using the NetworkX library to add a node to the visual graph
        self.graph.add_edge(r, s)
        self.steps.append(self.graph.copy())  # Store current step for visualization purposes

    # This will be called when a node is to be created
    def createElement(self, node):
            self.parent[node] = node
            # This is to add a node to the NetworkX layout graph
            self.graph.add_node(node)
            self.size[node] = 1

    # Prints list where each entry corresponds to specific node (ie. list[0] = node 0) which has value of parent of that node
    # Example: if nodes 0 to 3 have parent node 0 list will be { 0 0 0 0 }
    # Note: you can simply write print(self.parent) for the same effect, this is just a different format
    def printGraphList(self):
        string = "{ "
        for i in range(len(self.parent)):
            string += str(self.parent[i]) + " "
        string += "}"
        print(string)

def makeRandomGraph():
    # Get a random number of nodes n, within a specified range
    numNodes = rand.randint(1, maxNodes)
    # Get a random number of edges where the max number of edges is n - 1
    numEdges = rand.randint(0, numNodes - 1)
    print("Number of edges: " + str(numEdges) +"\nNumber of nodes: " + str(numNodes))
    unionfind = UnionFind(numNodes)
    # Create n nodes
    for i in range(numNodes):
        unionfind.createElement(i)
    # Create a random number of edges
    # This method means that nodes can still set their parent as themselves
    for i in range(numEdges):
        unionfind.union(rand.randint(0, numNodes - 1), rand.randint(0, numNodes - 1))
    return unionfind

# For test purposes
# Change the argument of displayGraph to this to change to this graph
def preMadeGraph():
    n = 10
    unionfind = UnionFind(n)
    for i in range(n):
        unionfind.createElement(i)
    unionfind.union(0, 2)
    unionfind.union(0, 3)
    unionfind.union(5, 6)
    unionfind.union(5, 7)
    unionfind.union(8, 7)
    unionfind.union(9, 1)
    return unionfind

# Simply displays the output and updates for each step as well as the list of parent values
# timer is in milliseconds
def displayGraph(graphToDisplay, delayTimer):
    graph, ax = plot.subplots()
    update = anim(graph, updateGraph, frames = len(graphToDisplay.steps), fargs = (ax, graphToDisplay), interval = delayTimer, repeat = False)
    graphToDisplay.printGraphList() # This call displays the graph parent list in the console
    plot.show()

# Updates graph for every step of the union
def updateGraph(step, graph, graphToDisplay):
    graph.clear() # Clears the graph so there is no 'overlap' between previous steps
    netx.draw_spring(graphToDisplay.steps[step], with_labels = True, node_size = 500, node_color = 'lightblue', font_size = 10, font_weight = 'bold', ax = graph)

    if step == 0: # If it is the initial graph, state that it's the inital graph in the title
        graph.set_title("Initial Graph", fontsize=12)
        return
    
    # Keep track of previous edges so we don't display them in current step
    # If we don't do this, it would show all previous unions in text
    previousUnions = graphToDisplay.steps[step - 1].edges()
    union = graphToDisplay.steps[step].edges()

    toDisplay = [edge for edge in union if edge not in previousUnions]
    # Create the axis title based on the connected nodes
    text = "Connected nodes " + ", ".join(f"{node1} and {node2}" for node1, node2 in toDisplay)
    # If final step, tell user that the process has fininished by having "done" at the end of string
    if step == len(graphToDisplay.steps) - 1:
        text += "\nDone!"
    graph.set_title(text, fontsize=12)    

displayGraph(makeRandomGraph(), 1000)