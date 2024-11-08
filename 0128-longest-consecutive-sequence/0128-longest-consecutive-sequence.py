class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n=len(nums)
        st=set()
        for i in nums:
            st.add(i)
        count=0
        long=0
        for i in st:
            if i-1 not in st:
                count=1
                x=i
                while x+1 in st:
                    x+=1
                    count+=1
                
                long=max(count,long)    
        return long            






        