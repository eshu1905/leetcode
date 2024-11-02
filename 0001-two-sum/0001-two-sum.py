class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[-1,-1]
        map={}
        s=0
        for i in range(len(nums)):
            s=nums[i]
            more=target-s
            if more in map:
                arr[0]=map[more]
                arr[1]=i
                return arr
            map[nums[i]]=i                                  






        