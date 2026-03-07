class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <=k:
        #             return True
        # return False
        index_map={}
        for current_index, value in enumerate(nums):
            if value in index_map and current_index-index_map[value] <= k:
                return True 
            index_map[value]=current_index
        return False