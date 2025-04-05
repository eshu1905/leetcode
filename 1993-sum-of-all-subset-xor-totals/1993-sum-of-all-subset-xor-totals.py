class Solution(object):
    def subsetXORSum(self, nums):
        res=0
        n = len(nums)
        result = []
        for i in range(1 << n):  # Loop from 0 to 2^n - 1
            ans=0
            subset = []
            for j in range(n):
                if i & (1 << j):  # Check if the j-th bit is set
                    subset.append(nums[j])
            for i in subset:
                ans^=i
            res+=ans
        return res        




        """
        :type nums: List[int]
        :rtype: int
        """
        