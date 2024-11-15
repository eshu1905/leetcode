class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=1
        sufix=1
        has=[0]*n
        for i in range(n):
            has[i]=prefix
            prefix*=nums[i]
        for i in range(n-1,-1,-1):
            has[i]*=sufix
            sufix*=nums[i]
        return has    


       