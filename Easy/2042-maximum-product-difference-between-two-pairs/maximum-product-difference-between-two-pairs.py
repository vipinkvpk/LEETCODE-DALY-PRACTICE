class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # from itertools import pairwise 
        # return max((a*b)-(c*d) for (a,b)(c,d) in pairwise(nums))
        nums.sort()
        max_product = nums[-1] * nums[-2]
        min_product = nums[0] * nums[1]
        return max_product - min_product