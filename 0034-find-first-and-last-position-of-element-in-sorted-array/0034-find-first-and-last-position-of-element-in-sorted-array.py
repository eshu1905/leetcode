class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        def first(nums,target):
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1    
                else:
                    low=mid+1
            return ans
        def last(nums,target):
            ans=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1    
                else:
                    low=mid+1
            return ans
        first=first(nums,target)
        second=last(nums,target)
        

    
        if first==-1:



            return [-1,-1]
        return[first,second]         


                    



                                