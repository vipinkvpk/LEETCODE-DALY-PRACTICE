class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # count=0
        # for i in nums:
        #     if i < k:
        #         count+=1
        # return count
        return sum(1 for num in nums if num<k)
        