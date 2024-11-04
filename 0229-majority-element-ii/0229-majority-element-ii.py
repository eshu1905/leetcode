class Solution(object):
    def majorityElement(self, nums):
        ls=[]
        n=len(nums)
        map={}
        counter=Counter(nums)
        for i,j in counter.items():
            if j>n//3:
                ls.append(i)
            if len(ls)==2:
                break
        return ls                                  
                               
        