class Solution(object):
    def maxSubArray(self, nums):
        maxi=float("-inf")
        sume=0
        for i in nums:
            sume+=i
            maxi=max(maxi,sume)
            if sume<0:
                sume=0
        return maxi          

        
        """
        :type nums: List[int]
        :rtype: int
        """
        