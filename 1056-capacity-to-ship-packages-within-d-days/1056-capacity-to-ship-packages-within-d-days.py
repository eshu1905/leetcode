class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        def weight(weights,mid,days):
            d=1
            w=0
            for i in weights:
                if w+i>mid:
                    d+=1
                    w=i
                else:
                    w+=i
            return d<=days
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            if weight(weights,mid,days):
                high=mid-1
            else:
                low=mid+1
        return low            


        