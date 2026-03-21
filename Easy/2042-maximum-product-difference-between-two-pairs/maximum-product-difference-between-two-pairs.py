class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # from itertools import pairwise 
        # return max((a*b)-(c*d) for (a,b)(c,d) in pairwise(nums))
        nums=sorted(nums)
        return (nums[-1]*nums[-2] - nums[0]*nums[1])