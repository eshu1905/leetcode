from collections import Counter
class Solution(object):
    def divideArray(self, nums):
        if len(nums)%2!=0:
            return False
        count=Counter(nums)
        for i,n in count.items():
            if n%2!=0:
                return False
            
        return True  

        """
        :type nums: List[int]
        :rtype: bool
        """
        