class Solution:
    def minimumSum(self, num: int) -> int:
        s= list(str(num))
        s.sort()
        sum1 = s[0]+s[3]
        sum2 = s[1]+s[2]
        return int(sum1) + int(sum2)