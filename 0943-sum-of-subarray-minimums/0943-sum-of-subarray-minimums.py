class Solution(object):
    def sumSubarrayMins(self, arr):
        
        MOD = 10**9 + 7
        n = len(arr)
    
    # Arrays to store left and right bounds
        left, right = [0] * n, [0] * n
    
    # Monotonic stack for left boundary (previous smaller element)
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
    
    # Monotonic stack for right boundary (next smaller element)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:  # '=' to avoid duplicate min count
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
    
    # Compute the sum of minimums in all subarrays
        result = sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD
        return result
        """
        :type arr: List[int]
        :rtype: int
        """
        