class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=nums[0]
        s=0
        c=-1
        for i in range(len(nums)):
            s+=nums[i]
            l=max(l,s)
            if s<0:
                s=0    
        return l       

        