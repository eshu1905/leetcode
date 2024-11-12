class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        k=extraCandies
        maxi=max(candies)
        arr=[]
        for i in range(n):
            if (candies[i]+k)>=maxi:
                arr.append(True)
            else:
                arr.append(False)
        return arr                  