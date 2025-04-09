class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string1=str(n)
        sum=0
        for i,v in enumerate(string1):
            digit=int(v)
            if i%2 == 0:
                sum+=digit
            else:
                sum-=digit
        return sum
        # sum=0
        # while n>0:
        #     digit=n%10
            
        #     sum+=digit
        #     n=n//10 
        # return sum
        