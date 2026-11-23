# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node = head
        nodes = []

        while node:
            nodes.append(node)
            node = node.next

        
        i, j = 0, len(nodes)-1

        while i<j:
            nodes[i].next = nodes[j]
            i+=1

            if i == j:
                break
            
            nodes[j].next = nodes[i]
            j-=1
        nodes[i].next = None
    
    
        
        