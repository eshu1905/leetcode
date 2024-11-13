class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=1
        rows=[1]
        for i in range(rowIndex):
            ans*=(rowIndex-i)
            ans=ans//(i+1)
            rows.append(int(ans))
        return rows    

        