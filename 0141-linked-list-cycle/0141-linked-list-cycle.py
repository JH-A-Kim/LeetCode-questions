# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        speed1, speed2 = head, head

        while speed2 and speed2.next:
            speed1 = speed1.next
            speed2 = speed2.next.next

            if speed1 == speed2:
                return True
        return False

# 1 -> 2