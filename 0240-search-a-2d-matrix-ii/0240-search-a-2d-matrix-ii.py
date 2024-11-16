class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if matrix[i][-1]<target:
                continue
            elif matrix[i][0]>target:
                break
            low=0
            high=m-1
            while(low<=high):
                mid=(low+high)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return False                 
        