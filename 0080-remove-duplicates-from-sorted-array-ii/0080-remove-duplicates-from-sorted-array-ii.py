class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        c=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                c+=1
            else:
                c=1
            if c<=2:
                nums[j]=nums[i]
                j+=1
        return j                