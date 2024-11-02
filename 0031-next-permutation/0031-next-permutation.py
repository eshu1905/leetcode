class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            return nums.reverse()
        for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
                break
        nums[index+1:]=reversed(nums[index+1:]) 
        return nums                   
        