from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq= Counter(s)

        max_odd = 0 
        min_even = float('inf')

        for f in freq.values():
            if f%2 == 0:
                min_even = min(min_even,f)
            else:
                max_odd = max(max_odd,f)

        return max_odd - min_even 

        