class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words =s.strip().split(" ")
        for word in words:
            
            last= words[-1]
            return len(last)