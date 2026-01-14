class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # new=""
        # for i in range(len(s)):
        return s[:k][::-1] + s[k:]

        
        