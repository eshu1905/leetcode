class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                hashset=set()
                for k in range(j+1,n):
                    more=target-(nums[i]+nums[j]+nums[k])
                    if more in hashset:
                        temp=[nums[i],nums[j],nums[k],more]
                        temp.sort()
                        st.add(tuple(temp))
                    hashset.add(nums[k])

        ans=list(st)
        return ans                        
        
        