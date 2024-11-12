class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x1=x
        x2=0
        while x1>0:
            x2=x2*10+x1%10
            x1//=10   
        if x2==x:
            return True
        return False           
        