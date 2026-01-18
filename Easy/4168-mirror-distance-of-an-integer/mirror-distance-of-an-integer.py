class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = str(n)[::-1]
        return abs(n-int(rev))


    # def reverse(self, n:int):
    #     reversed_number=0
    #     while (n>0):
    #         last_digit=n%10
    #         reversed_number = reversed_number * 10 + last_digit
    #         n=n//10
    # def mirrorDistance(self, n: int) -> int:
    #     rev = self.reverse(n)
    #     return abs(n-rev)
        