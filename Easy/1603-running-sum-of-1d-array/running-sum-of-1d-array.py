class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        total=0
        for x in nums:
            total+=x 
            res.append(total)
        return res
        