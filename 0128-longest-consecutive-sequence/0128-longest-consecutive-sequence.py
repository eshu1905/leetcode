class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        lastsmall=-2**31
        count=0
        long=1
        n=len(nums)
        for i in range(n):
            if nums[i]-1==lastsmall:
                count+=1
                lastsmall=nums[i]
            elif nums[i]!=lastsmall:
                count=1
                lastsmall=nums[i]
            else:
                pass    
            long=max(long,count)
        return long            




        