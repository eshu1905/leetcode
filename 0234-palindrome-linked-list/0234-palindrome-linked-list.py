# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        stack=[]
        temp=head
        while temp:
            stack.append(temp.val)
            temp=temp.next
        res=[]
        for i in reversed(stack):
            res.append(i)
        return stack==res        
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        