class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=0
        num2=0
        for i in range(n+1):
            if (i%m) != 0:
                num1+=i
            else:
                num2+=i
            sum=num1-num2
        return sum




#====================

#Optimized

# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         total_sum = (n * (n + 1)) // 2
#         k = n // m
#         divisible_sum = m * (k * (k + 1)) // 2
#         return total_sum - 2 * divisible_sum


        