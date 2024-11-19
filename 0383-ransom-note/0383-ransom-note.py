class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n=len(ransomNote)
        for i in range(n):
            if ransomNote[i] not in magazine+magazine:
                return False
            else:
                magazine=magazine.replace(ransomNote[i]," ",1)
                   
        return True        
        