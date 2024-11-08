import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        
        def divisors(nums,mid,threshold):
            c=0
            for i in range(n):
                c+=math.ceil(nums[i]/mid)
            return c<=threshold
        low=1
        high=max(nums)
        while(low<=high):
            mid=(low+high)//2
            if divisors(nums,mid,threshold):
                high=mid-1
            else:
                low=mid+1
        return low                  
        