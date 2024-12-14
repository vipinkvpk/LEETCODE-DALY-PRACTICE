class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # res=""
        # for str in words:
        #     pword=str[::-1]
        #     print(pword)
        #     if str == pword:
        #         res.add(pword)
        #         return str
        #     else:
        #         continue
        # return False
        for word in words:
            if word == word[::-1]:
                return word
        return ""