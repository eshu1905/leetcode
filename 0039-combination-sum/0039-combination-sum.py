class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def possible(index,current,target):
            if index>=n:
                if target==0:
                    result.append(current[:])
                else:
                    return
                return 
            if candidates[index]<=target:
                current.append(candidates[index])
                possible(index,current,target-candidates[index])
                current.remove(candidates[index])
            possible(index+1,current,target)
        result=[]
        possible(0,[],target)
        return result           
        