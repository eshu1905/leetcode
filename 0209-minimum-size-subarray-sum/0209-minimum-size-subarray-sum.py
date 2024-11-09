class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l,r,ans=0,0,float("inf")
        s=0
        while(r<n):
            s+=nums[r]
            r+=1
            while(s>=target):
                ans=min(ans,r-l)
                s-=nums[l]
                l+=1
        return ans if ans!=float("inf") else 0        
                



        