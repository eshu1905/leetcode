class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtracking(index,current):
            if index==len(nums):
                if current[:] not in result:
                    result.append(current[:])
                return
            for end in range(index,len(nums)):
                current[end],current[index]=current[index],current[end]
                backtracking(index+1,current)
                current[end],current[index]=current[index],current[end]
            return result
        return backtracking(0,nums)

                    
        