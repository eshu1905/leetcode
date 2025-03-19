class Solution(object):
    def minOperations(self, nums):
        lenght=len(nums)
      
        cnt = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                cnt += 1
                nums[i+1] = 0 if nums[i+1] == 1 else 1
                nums[i+2] = 0 if nums[i+2] == 1 else 1
        return cnt if nums[-1] and nums[-2] else -1     

        """
        :type nums: List[int]
        :rtype: int
        """
        