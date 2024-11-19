class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0
        current_sum = 0
        start = 0
        unique_elements = set()

        for end in range(n):
            # Slide the window to maintain distinct elements
            while nums[end] in unique_elements or len(unique_elements) >= k:
                unique_elements.remove(nums[start])
                current_sum -= nums[start]
                start += 1

            # Add the current element to the set and update the sum
            unique_elements.add(nums[end])
            current_sum += nums[end]

            # Check if the window has size k
            if len(unique_elements) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum

        
                        
                




        