class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sum=0
        for num in nums:
            if num%3 !=0:
                sum+=1
        return sum