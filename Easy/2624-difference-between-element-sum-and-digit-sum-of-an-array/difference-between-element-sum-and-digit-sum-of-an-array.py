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


        

# The while loop is used to extract each digit of the number:
# % 10 gives the last digit.
# // 10 removes the last digit from the number.
# This loop continues until the number becomes 0.
# The extracted digit is then added to the digit_sum.

# #Time complexity of above solution-O(N) -Already optimized

# Beats73.02%


# Space Complexity:
# Storing sum_nums and digit_sum uses O(1) space.
# No additional data structures are used, so the overall Space Complexity is O(1).
