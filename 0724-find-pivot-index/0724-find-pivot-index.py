class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        pivot1=0
        pivot2=0
        for i in range(n):
            prefix[i]=pivot1
            pivot1+=nums[i]
        for i in range(n-1,-1,-1):
            suffix[i]=pivot2
            pivot2+=nums[i] 
        for i in range(n):
            if prefix[i]==suffix[i]:
                return i
        return -1               
        