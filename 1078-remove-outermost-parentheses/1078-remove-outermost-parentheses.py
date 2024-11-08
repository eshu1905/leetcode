class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=""
        balence=0
        for i in s:
            if i=="(":
                if balence>0:
                    result+=i
                balence+=1
            elif i==")":
                balence-=1
                if balence>0:
                    result+=i   
        return result                                


            


        