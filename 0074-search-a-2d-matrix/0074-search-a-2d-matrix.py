class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[num for row in matrix for num in row]
        if target in arr:
            return True
        return False    
        