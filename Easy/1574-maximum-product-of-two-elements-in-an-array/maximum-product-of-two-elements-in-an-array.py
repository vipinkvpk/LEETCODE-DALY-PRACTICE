class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lar=seclar=0
        n=len(nums)
        for i in range(n):
            if nums[i] > lar:
                seclar=lar
                lar=nums[i]
                lar=lar-1
            elif nums[i]>seclar:
                seclar =nums[i]
                seclar=seclar-1
            
        return (lar)*(seclar)
        