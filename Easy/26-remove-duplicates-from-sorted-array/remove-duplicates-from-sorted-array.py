class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j