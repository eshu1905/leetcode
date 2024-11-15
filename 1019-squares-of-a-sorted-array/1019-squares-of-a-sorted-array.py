class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            k=nums[i]**2
            nums[i]=k
        nums.sort()
        return nums    
        