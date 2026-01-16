class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in nums:
            if (i%2)==0:
                i=0
                even.append(i)
            else:
                i=1
                odd.append(i)
        return even + odd
        