class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        # for i in range(n):
        #     if (n*(n+1)/2)!=sum(nums):
        #         return -sum(nums)
        expected_sum=(n*(n+1))//2
        actual_sum=sum(nums)
        return expected_sum-actual_sum