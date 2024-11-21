class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        def backtracking(index,current):
            if index==n:
                result.append(current[:])
                return

            
            for i in range(index,n):
                current[index],current[i]=current[i],current[index]
                backtracking(index+1,current)
                current[index],current[i]=current[i],current[index]
            
        backtracking(0,nums)
        return result                
        