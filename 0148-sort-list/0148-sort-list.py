# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        def middle(heads):
            if  not heads or not heads.next:
                return heads
            slow=heads
            fast=heads.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def mergeList(list1,list2):
            dummy=ListNode(0)
            k=dummy
            while list1 and list2:
                if list1.val<=list2.val:
                    dummy.next=list1
                    list1=list1.next
                else:
                    dummy.next=list2
                    list2=list2.next
                dummy=dummy.next

            if list1:
                dummy.next=list1
            else:
                dummy.next=list2
            return k.next              
        if not head or not head.next:
            return head
        middlenode=middle(head)
        lefthead=head
        righthead=middlenode.next
        middlenode.next=None
        left=self.sortList(lefthead)
        right=self.sortList(righthead)
        return mergeList(left,right)
        
               
        



        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        