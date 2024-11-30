
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        i, j = 0, len(nums) - 1
        while i < j:
            temp = nums[i] + nums[j]
            if temp == k:
                i += 1
                j -= 1
                ans += 1
            elif temp > k:
                j -= 1
            else:
                i += 1
        return ans
        