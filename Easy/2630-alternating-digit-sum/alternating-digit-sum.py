class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string1=str(n)
        total=0
        for i,v in enumerate(string1):
            digit=int(v)
            if i%2 == 0:
                total+=digit
            else:
                total-=digit
        return total
 