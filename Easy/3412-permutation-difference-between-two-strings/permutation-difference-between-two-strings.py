class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s1=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    s1+=abs(i-j)
        return s1
        