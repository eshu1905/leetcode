class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start==goal:
            return 0
        ans=start^goal
        c=0
        while ans!=0:
            ans=ans&(ans-1)
            c+=1
        return c       
    
        

        