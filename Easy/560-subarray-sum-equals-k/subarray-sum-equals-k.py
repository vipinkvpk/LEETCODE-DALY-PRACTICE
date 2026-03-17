class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # n=len(nums)
        # for i in range(len(nums)):
        #     s=0
        #     for j in range(i,n):
        #         s+=nums[j]
        #         if s==k:
        #             count += 1
        # return count
        count = 0
        prefix_map = {0:1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if (curr_sum-k) in prefix_map:
                count += prefix_map[curr_sum-k]
            
            if curr_sum in prefix_map:
                prefix_map[curr_sum] += 1
            else:
                prefix_map[curr_sum] = 1
        return count
        

        