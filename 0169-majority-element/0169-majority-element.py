class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        e=None
        for i in range(len(nums)):
            if c==0:
                c=1
                e=nums[i]
            elif e==nums[i]:
                c+=1
            else:
                c-=1
        return e            


        