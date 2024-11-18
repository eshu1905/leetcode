class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        result=[0]*n
        if k==0:
            return result
        start,end,step=(1,k+1,1) if k>0 else (k,0,1)
        for i in range(n):
            result[i]=sum(code[(i+j)%n] for j in range(start,end,step))
        return result        
                  
        