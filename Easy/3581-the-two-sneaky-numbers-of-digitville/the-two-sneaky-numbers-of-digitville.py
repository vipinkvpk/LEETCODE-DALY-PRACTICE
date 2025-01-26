class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        unique=set()
        res=[]
        for i in nums:
            if i in unique:
                res.append(i)
            else:
                unique.add(i)
        return res


        