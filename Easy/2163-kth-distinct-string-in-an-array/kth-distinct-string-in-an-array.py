class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        freq= Counter(arr)
        distinct_count=0
        for ch in arr:
             
            if freq[ch]==1:
                distinct_count+=1
                if distinct_count==k:
                    return ch 
        return ""
        