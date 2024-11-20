class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k=len(flowerbed)
        if k==1 and flowerbed[0]==0:
            return True
        for i in range(k):
            if i==0 and i+1<k and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            elif i==k-1 and i-1>=0 and flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n-=1
            elif flowerbed[i]==0 and i+1<k and i-1>=0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1


        print(flowerbed)
        if n<=0:
            return True
        return False                

        