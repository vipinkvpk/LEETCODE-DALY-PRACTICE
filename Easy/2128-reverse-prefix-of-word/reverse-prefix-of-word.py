class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word:
            res=""
            # suffix=""
            for i in range(len(word)):     
                if word[i]==ch:
                    prefix= word[0:i+1]
                    suffix=word[i+1:]
                    res+= prefix[::-1] + suffix
                    break
            return res
            
        return  word
            





        