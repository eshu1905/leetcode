class Solution(object):
    def generate(self, numRows):
        def getRow(row):
            ans=1
            store=[1]
            for col in range(1,row):
                ans*=(row-col)
                ans=ans//col
                store.append(ans)
            return store
        get=[]
        for i in range(1,numRows+1):
            get.append(getRow(i))
        return get                   