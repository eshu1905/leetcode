class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        first,last=-1,-1
        ls=[]
        for i in range(n):
            if nums[i]==target:
                if first==-1:   
                    first=i
                last=i
        return [first,last]        
                                