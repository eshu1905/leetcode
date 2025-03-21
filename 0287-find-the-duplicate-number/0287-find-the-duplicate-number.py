class Solution(object):
    def findDuplicate(self, nums):
        hmap={}
        for i in nums:
            if i in hmap:
                return i
            hmap[i]=1           

        """
        :type nums: List[int]
        :rtype: int
        """
        