class Solution:
    def minimumSum(self, num: int) -> int:
        s= list(str(num)) #1. converting an integer to string and then to list (int -> str -> list)
        s.sort() #(2. sorting the list)
        sum1 = s[0]+s[3] # 3. string concatenation
        sum2 = s[1]+s[2]
        return int(sum1) + int(sum2) #4. convert back str -> int  ,add and then return