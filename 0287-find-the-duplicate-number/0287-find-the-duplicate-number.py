class Solution(object):
    def findDuplicate(self, nums):
        hmap={}
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        for i,n in hmap.items():
            if n>1:
                return i
        return None        

        """
        :type nums: List[int]
        :rtype: int
        """
        