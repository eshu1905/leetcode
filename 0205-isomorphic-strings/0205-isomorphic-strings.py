class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        map1={}
        map2={}

        for i in range(n):
            if ((s[i] in map1 and map1[s[i]]!=t[i]) or (t[i] in map2 and map2[t[i]]!=s[i])):
                return False
            map1[s[i]]=t[i]
            map2[t[i]]=s[i]
        return True               


        