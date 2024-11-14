class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        altitudes=[0]*(n+1)
        one=0
        for i in range(n):
            one+=gain[i]
            altitudes[i+1]=one
        maxi=max(altitudes)
        return maxi    
        