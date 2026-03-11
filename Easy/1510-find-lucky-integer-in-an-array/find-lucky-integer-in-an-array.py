class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        freq = Counter(arr)
        lucky = -1
        for x,v in freq.items():
            if x == v:
                lucky = max(lucky,x)
        return lucky
                
        