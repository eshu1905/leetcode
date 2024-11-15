from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map={}
        n=len(nums)
        for i in range(n):
            if nums[i] in map:
                return True
            map[nums[i]]=1
        return False        
                

        