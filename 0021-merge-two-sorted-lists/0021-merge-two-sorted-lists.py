# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        placeholder = ListNode()

        newList = placeholder

        while list1 and list2:
            if list1.val<=list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next # we are now at the current added value in this step.
        
        # and then we need to add the rest of the leftover list thats super simple because of the property of linked lists
        newList.next = list1 or list2

        return placeholder.next
        