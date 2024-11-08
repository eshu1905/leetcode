class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def possible(nums,k,mid):
            count=1
            high=0
            for i in range(n):
                if high+nums[i]>mid:
                    count+=1
                    high=nums[i]
                else:
                    high+=nums[i]
            return count>k
        low=max(nums)
        high=sum(nums)
        while(low<=high):
            mid=(low+high)//2
            if possible(nums,k,mid):
                low=mid+1
            else:
                high=mid-1
        return low                                
        