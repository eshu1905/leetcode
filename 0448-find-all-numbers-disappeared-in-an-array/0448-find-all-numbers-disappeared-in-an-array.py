class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        s=set()
        for i in nums:
            s.add(i)
        for i in range(1,n+1):
            if i not in s:
                ans.append(i)
        return ans        


        