class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums1=[]
        for i in range(len(nums)):
            nums1.append(nums[nums[i]])
        return nums1


        