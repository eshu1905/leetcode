class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)
        for i in range(n):
            if n==1:
                return nums[0]
            if i==0 and nums[i]!=nums[i+1]:
                return nums[i]
            elif i==n-1 and nums[i]!=nums[i-1]:
                return nums[i]
            else:
                if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                    return nums[i]                               
            