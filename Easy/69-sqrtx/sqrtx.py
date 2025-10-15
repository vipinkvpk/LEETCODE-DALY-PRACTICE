import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<0:
            return None 
        else:
            return floor(math.sqrt(x))
        