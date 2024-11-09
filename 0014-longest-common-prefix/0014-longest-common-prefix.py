class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini=float("inf")
        i=0
        for s in strs:
            if len(s)<mini:
                mini=len(s)
        while(i<mini):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]                               
        