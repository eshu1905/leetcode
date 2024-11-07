class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        mini=nums[0]
        for i in range(n):
            if nums[i]<mini:
                mini=nums[i]
        return mini        