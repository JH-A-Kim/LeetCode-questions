# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
        # at each point we reverse the direction of the pointer so that when we are at head.next we point it to the node from the previous iteration and then move the previous node to the current head that we are at where prev is also becoming the head of our linkedlist and then we move the head to the saved value and then do it again. TLDR we take a value reverse its direction but before that we save its next stop and then take that next value independently and eventually head = None because its at the tail. and prev is now the head of this new array. 


        

