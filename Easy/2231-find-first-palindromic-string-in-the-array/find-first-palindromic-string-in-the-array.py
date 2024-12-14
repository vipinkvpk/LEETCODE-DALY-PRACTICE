class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res=""
        for word in words:
            revw=word[::-1]
            
            if revw == word:

                return word

        return ""
        # for word in words:
        #     if word == word[::-1]:
        #         return word
        # return ""