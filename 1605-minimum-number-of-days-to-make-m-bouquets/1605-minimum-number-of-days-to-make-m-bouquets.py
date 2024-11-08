class Solution(object):
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        low=min(bloomDay)
        high=max(bloomDay)
        val=m*k
        if val>n:
            return -1
        while(low<=high):
            mid=(low+high)//2
            
            if self.possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low
    def possible(self,bloomDay,f,m,k):
        count=0
        boc=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=f:
                count+=1
            else:
                boc+=(count//k)
                count=0
        boc+=(count//k)
        if boc>=m:
            return True
        else:
            return False                                               

        