class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # from itertools import pairwise
        # is_pair = all((a,b) for a,b in pairwise(nums))
        # return is_pair

        freq_count = Counter(nums)
        # for v in count.values():
        #     if v%2==0:
        #         return True 
        #     return False
        return all(count%2==0 for count in freq_count.values())
        