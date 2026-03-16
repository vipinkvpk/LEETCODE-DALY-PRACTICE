class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = []

        from collections import Counter 
        freq = Counter(nums)
        for x, v in freq.items():
            if v > n/3:
                lst.append(x)
        return lst
        