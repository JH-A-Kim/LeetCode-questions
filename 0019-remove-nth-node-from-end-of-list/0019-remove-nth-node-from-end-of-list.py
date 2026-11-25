# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        right = head
        left = dummy

        while n>0: # this creates an offset so that when right reaches none then left will always be n+1 spaces away from the end therefore meaning left is now always at the value before n. this means we just need to set left.next = left.next.next
            right = right.next
            n-=1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next