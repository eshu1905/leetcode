from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst=s.split()
        n1=len(lst)
        n2=len(pattern)
        m1={}
        m2={}
        if n1!=n2:
            return False
        for i in range(n1):
            if (pattern[i] in m1 and  m1[pattern[i]]!=lst[i] or lst[i] in m2 and m2[lst[i]]!=pattern[i]):
                return False
            m1[pattern[i]]=lst[i]
            m2[lst[i]]=pattern[i]
        return True        


        
        