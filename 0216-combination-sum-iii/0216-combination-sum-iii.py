class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n:
            return []
        nums=[num for num in range(1,10)]
        def possible(index,current,sum):
            if index==len(nums):
                if sum==n:
                    if len(current[:])==k:
                        result.append(current[:])
                    else:
                        return
                else:
                    return        
                return
            current.append(nums[index])
            sum+=nums[index]
            possible(index+1,current,sum)
            current.remove(nums[index])
            sum-=nums[index]
            possible(index+1,current,sum)
        result=[]                
        possible(0,[],0)
        return result