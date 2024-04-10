# COMP359 - Assignment 3 - Union-Find Algorithm and Visualization
<p>This project implements the Union-Find algorithm with the Python programming language.<br>
Visualization is done with the help of Matplotlib and NetworkX.<br></p>

The algorithm itself has find implemented with path compression and union by size.  
# The Find() Algorithm (With Path Compression)
<p>The find() function simply finds the root node of the tree which the current node (which is passed as a parameter) is attached to.<br>
Path compression is done by recursively calling the find() function until we reached the root node of the tree (a node which is its own parent).<br>
This means that each node should point to the root node of the tree which becomes its parent, compressing the path to the root node by simply pointing directly to the root node.

> If we assume some node 3 has a parent 9.  
> By the function call with find(3), the value returned will be 9.  
> Thus, find(3) = 9.
</p>

# The Union() Algorithm (Union by Size)
<p> The union algorithm at the most basic level simply combines two subtrees into a single tree sharing the same root.<br>
Complications will arise when determining which node during the union should become the parent of the other node.<br>
In this implementation, this choice is made based on size, hence the name "Union by Size". Between the two nodes that are being unioned together, which node has is part of a tree with more nodes should become the parent of the other node. If two nodes are in trees of equal size, it does not matter which node becomes the parent.

> If we want to union some nodes 5 and 6, we would make a function call union(5, 6).  
> For this example, assume the subtree node 6 is connected to is bigger than the subtree node 5 is connected to.  
> Union by size means that the new parent of node 5 is now node 6.
</p>


# References  

NetworkX. (n.d.). NetworkX reference — NetworkX documentation. https://networkx.org/documentation/stable/reference/index.html  
Matplotlib. (n.d.). Matplotlib: Visualization with Python. https://matplotlib.org/stable/index.html  
GeeksforGeeks. (n.d.). Introduction to disjoint set data structure or union-find algorithm. https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
