# COMPLEXITY-O(N*2)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        tar=[]
        for i in range(len(nums)):
            for i in range(len(index)):
                tar.insert(index[i],nums[i])
            return tar


# ++++++++++++++++++++++++++++++
#COMPLEXITY -O(N)
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         tar=[]
#         for i in range(len(nums)):
#             # for i in range(len(index)):
                
#             tar.insert(index[i],nums[i])
#         return tar
        