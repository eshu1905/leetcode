# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        