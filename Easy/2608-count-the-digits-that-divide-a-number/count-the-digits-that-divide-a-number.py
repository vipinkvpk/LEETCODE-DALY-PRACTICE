class Solution:
    def countDigits(self, num: int) -> int:
        str_num=str(num)
        count = 0
        for s in str_num:
            if num % int(s) == 0:
                count+=1 
        return count


        