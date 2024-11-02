class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        nums[len(nums)-k:]=reversed(nums[len(nums)-k:])
        nums[:len(nums)-k]=reversed(nums[:len(nums)-k])
        return nums.reverse()
       
        """
        Do not return anything, modify nums in-place instead.
        """
        