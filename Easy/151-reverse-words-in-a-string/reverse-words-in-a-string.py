class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        # return " ".join(reversed(words))
        words=words[::-1]
        return " ".join(words)
        