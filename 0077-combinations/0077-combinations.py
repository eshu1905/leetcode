class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst=[num for num in range(1,n+1)]
        result=[]
        def backtracking(index,current):
            if index>=len(lst):
                if len(current[:])==k:
                    result.append(current[:])
                else:
                    return    
                return    
            current.append(lst[index])
            backtracking(index+1,current)
            current.pop()
            backtracking(index+1,current)
        backtracking(0,[])
        return result            
        