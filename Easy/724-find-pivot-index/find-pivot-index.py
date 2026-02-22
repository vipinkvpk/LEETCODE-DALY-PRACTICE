class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)

        for i, x in enumerate(nums):
            right = right-x
            if left == right:
                return i 
            left += x 
        return -1
            
        