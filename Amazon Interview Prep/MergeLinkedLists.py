# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList=ListNode() #initialize a new set

        tracker=newList #tracker to go through the linked list

        while(list1!=None or list2!=None): # if any list objects exist we can go through the list
            if(list1!=None and list2!=None and list1.val>list2.val): # if both lists exist and list1.val is greater than list2.val append val 2 to the new list
                tracker.next=ListNode(list2.val, None)
                tracker=tracker.next # go to next
                list2=list2.next # go to next 
            elif(list1!=None and list2!=None and list1.val<=list2.val): # same but other way
                tracker.next=ListNode(list1.val, None)
                tracker=tracker.next
                list1=list1.next

            while(list1!=None and list2==None): #dumps rest of the linked list values
                tracker.next=ListNode(list1.val, None)
                tracker=tracker.next
                list1=list1.next
            while(list2!=None and list1==None): # dumps rest of the linked list values
                tracker.next=ListNode(list2.val, None)
                tracker=tracker.next
                list2=list2.next
            
                

        return newList.next # returns next node from head of initilized node
    # runs in O(n*m) because dumps will always be less than n 
    # it ran in 0ms beating 100% while taking 17.37 mb of memory beating 38.21% performance heavy not memory optimizied