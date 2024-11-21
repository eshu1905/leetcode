class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        result=[]
        def backtracking(index,current):
            if index==n:
                result.append(current[:])
            for i in range(index+1,n+1):
                if s[index:i]==s[index:i][::-1]:
                    backtracking(i,current+[s[index:i]])
        backtracking(0,[])
        return result
