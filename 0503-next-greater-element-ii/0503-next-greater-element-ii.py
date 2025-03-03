class Solution(object):
    def nextGreaterElements(self, nums):
        
        lenght=len(nums)
        ans=[-1]*lenght
        stack=[]
        for i in range(2*(lenght)-1,-1,-1):
            while stack and stack[-1]<=nums[i%lenght]:
                stack.pop()
            if i<lenght:
                if stack:
                    ans[i]=stack[-1]
                
            stack.append(nums[i%lenght])        
        return ans                


              