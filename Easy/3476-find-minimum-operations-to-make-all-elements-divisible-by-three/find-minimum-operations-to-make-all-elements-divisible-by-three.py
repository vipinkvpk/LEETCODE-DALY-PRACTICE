class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            remainder=i%3
            if remainder==1:
                count+=1     
            elif remainder==2:
                count+=1
        return count
