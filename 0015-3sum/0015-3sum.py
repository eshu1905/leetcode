class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        ls=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    ls.append([nums[i],nums[j],nums[k]])
                    while(j<k and nums[j]==nums[j+1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1        
                elif sum<0:
                    j+=1
                else: 
                    k-=1
                
        return ls                        


        