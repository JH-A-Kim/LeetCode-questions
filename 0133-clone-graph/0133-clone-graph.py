"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None: # basic check for if the node is none
            return None

        seen = {} # checks for if we already visited a node

        def dfs(old_node): # dfs solution for navigating through the graph
            if old_node in seen: # if we have already seen the node we just return what we have already seen, acts as a base case
                return seen[old_node]
            clone = Node(old_node.val) # creates a clone of the value if we have not seen it and puts it in the seen hash
            seen[old_node] = clone

            for neighbor in old_node.neighbors: # now for the value that we are at we look at the array which represents its neighbors and then we add each recursively sent value to its neighbor array
                clone.neighbors.append(dfs(neighbor))
            return clone # we then return the clone that we made of each node 

        return dfs(node)


        # we only create clones when we have not seen a value after we have the hash acts as a way to connect the graph to the clones and not the original graph