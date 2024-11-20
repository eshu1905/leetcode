class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, current):
        # Base case: if we've considered all elements
            if index == len(nums):
                result.append(current[:])  # Append a copy of the current subset
                return
        
        # Include the current element
            current.append(nums[index])
            backtrack(index + 1, current)
        
        # Exclude the current element (backtrack)
            current.pop()
            backtrack(index + 1, current)
    
        result = []
        backtrack(0, [])
        return result

        