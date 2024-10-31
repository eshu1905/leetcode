class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for i in range(len(nums)):
            map[nums[i]]=map.get(nums[i],0)+1
        for num,count in map.items():
            if count>len(nums)/2:
                return num   
        