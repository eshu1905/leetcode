class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)):
            if needle in haystack[i:n+i]:
                return i
                break          
        return -1