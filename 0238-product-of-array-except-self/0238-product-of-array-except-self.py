class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        pre=1
        for i in range(n):
            result[i]=pre
            pre*=nums[i]
        sufix=1
        for i in range(n-1,-1,-1):
            result[i]*=sufix
            sufix*=nums[i]
        return result    


        