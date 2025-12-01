class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # common = []
        # for num in nums1:
        #     if num in nums2:
        #     # common.append(num)
        #         return num
        inter = set(nums1).intersection(set(nums2))
        if len(inter)>0:
            return min(inter)
        else:
            return -1
