class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        st=set()
        for i in range(n):
            st.add(nums[i])
        long=1
        for j in st:
            if j-1 not in st:
                count=1
                x=j
                while x+1 in st:
                    x+=1
                    count+=1
                long=max(long,count)
        return long                    





        