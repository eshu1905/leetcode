# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        dummynode=ListNode(-1)
        dummyhead=dummynode
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                dummynode.next=temp1
                nextnode=temp1.next
                dummynode=temp1
                temp1=nextnode
                
            else:
                dummynode.next=temp2
                nextnode=temp2.next
                dummynode=temp2
                temp2=nextnode
        while temp1:
            dummynode.next=temp1
            nextnode=temp1.next
            dummynode=temp1
            temp1=nextnode
        while temp2:
            dummynode.next=temp2
            nextnode=temp2.next
            dummynode=temp2
            temp2=nextnode
        if dummyhead.next:
            return dummyhead.next                



        