class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=0
        maxi=float("-inf")
        n=len(nums)
        s=0
        for i in range(n):
            s+=nums[i]
            c=1
            maxi=max(maxi,s)
            if c==0:
                s+=nums[i]
                c=1
            if s<0:
                c=0
                s=0

        return maxi            

        