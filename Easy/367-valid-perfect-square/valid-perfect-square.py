class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq= num**0.5
        if sq%2 == 0 or sq%2 ==1:
            return True 
        return False
        
        