class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if  (i<=j and nums[i]<=nums[j]) or (j<=i and nums[i] >= nums[j]):
        #             return True 
        #         return False

        from itertools import pairwise
        is_ascending = all(a<=b for a,b in pairwise(nums))
        is_descending = all(b<=a for a,b in pairwise(nums))
        return is_ascending or is_descending
