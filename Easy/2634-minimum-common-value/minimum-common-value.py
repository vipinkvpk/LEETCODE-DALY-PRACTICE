class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # common=[]
        # for i in nums1:
        #     if i in nums2:
        #         common.append(i)
        # return min(common)
        common=list(set(nums1) & set(nums2))
        if not common:
            return -1
        else:
            return min(common)
            

        
            

                
        