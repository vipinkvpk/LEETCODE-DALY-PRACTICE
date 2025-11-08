class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1=""
        str2=""
        for char in word1:
            str1+=char
        for ch in word2:
            str2+=ch
        if str1== str2:
            return True
        else:
            return False
