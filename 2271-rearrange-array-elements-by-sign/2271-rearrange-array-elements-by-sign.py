class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        for i in range(len(nums)):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)//2):
            nums[i*2]=positive[i]
            nums[(i*2)+1]=negative[i]
        return nums                
        