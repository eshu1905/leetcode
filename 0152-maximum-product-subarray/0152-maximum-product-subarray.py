class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        maxi=-2**31
        prefix=1
        sufix=1
        for i in range(n):
            if prefix==0:
                prefix=1
            if sufix==0:
                sufix=1
            prefix*=nums[i]
            sufix*=nums[n-i-1]
            maxi=max(maxi,max(prefix,sufix))
        return maxi            