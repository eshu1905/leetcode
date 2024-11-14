from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        occurences=list(counter.values())
        return len(occurences)==len(set(occurences))  
                          
        