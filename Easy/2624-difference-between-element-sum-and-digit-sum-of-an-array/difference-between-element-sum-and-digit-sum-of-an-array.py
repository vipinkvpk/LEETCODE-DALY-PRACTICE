class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        digit_sum=0
        for num in nums:
            while num>0:
                digit=num%10
                digit_sum+=digit
                num=num//10
        return abs(sum_nums-digit_sum)


        