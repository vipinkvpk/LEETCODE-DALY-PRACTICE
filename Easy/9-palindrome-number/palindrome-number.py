class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False 
        else:
            x_string= str(x)
            if x_string == x_string[::-1]:
                return True 
            return False
        