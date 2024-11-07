class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k):
            t=0
            for i in piles:
                t+=ceil((i)/k)
            return t
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            if time(mid)<=h:
                high=mid-1
            else:
                low=mid+1
        return low        

        