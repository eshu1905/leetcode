class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        p,n=0,1
        for i in range(len(nums)):
            if nums[i]>0:
                arr[p]=nums[i]
                p+=2
            else:
                arr[n]=nums[i]
                n+=2
        nums=arr
        return nums            
       