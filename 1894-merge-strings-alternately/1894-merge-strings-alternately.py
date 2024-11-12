class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        n1=len(word1)
        n2=len(word2)
        maxi=max(n1,n2)
        for i in range(maxi):
            if i<=n1-1:
                result+=word1[i]
            if i<=n2-1:
                result+=word2[i]
        return result        


        