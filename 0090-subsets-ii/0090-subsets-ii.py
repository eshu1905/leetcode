class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtracking(index,current):
            if index>=len(nums):
                if current[:] not in result:
                    result.append(current[:])
                   
                return
            current.append(nums[index])
            backtracking(index+1,current)
            current.pop()
            backtracking(index+1,current)
        result=[]
        backtracking(0,[])
        return result

        