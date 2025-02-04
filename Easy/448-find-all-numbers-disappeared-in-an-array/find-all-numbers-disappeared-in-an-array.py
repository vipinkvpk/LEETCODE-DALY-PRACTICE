class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique=set(nums)
        missing=[]
        n=len(nums)
        for i in range(1,n+1):
            if i not in unique:
                missing.append(i)

        return missing
        