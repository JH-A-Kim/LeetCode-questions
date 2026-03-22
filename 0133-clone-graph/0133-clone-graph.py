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
        
        if node is None:
            return None

        seen = {}

        def dfs(old_node):
            if old_node in seen:
                return seen[old_node]
            clone = Node(old_node.val)
            seen[old_node] = clone

            for neighbor in old_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)


        