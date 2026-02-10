class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # return n
        odd_num=1
        odd_sum=0 
        for i in range(n):
            odd_sum+=odd_num 
            odd_num+=2 
        
        even_num=2
        even_sum=0
        for i in range(n):
            even_sum+=even_num
            even_num+= 2

        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a 
        return gcd(odd_sum, even_sum)
            
        