from bisect import bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n=len(nums)
        nums.sort()
        c=0
        for i in range(n):
            j=bisect_left(nums,lower-nums[i],i+1)
            k=bisect_left(nums,upper-nums[i]+1,i+1)
            c+=k-j
        return c    
                                                       