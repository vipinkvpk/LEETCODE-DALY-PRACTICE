class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        special_sqare_list=[]

        for i in range(1,n+1):
            if n%i == 0:
                nums_square=nums[i-1]*nums[i-1]
                special_sqare_list.append(nums_square)

        return sum(special_sqare_list)
