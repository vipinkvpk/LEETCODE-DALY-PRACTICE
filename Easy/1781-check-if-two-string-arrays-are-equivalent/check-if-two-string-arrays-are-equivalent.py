class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # for word in word1:
        #     comb1="".join(word1)

        # for word in word2:
        #     comb2="".join(word2)
        comb1=""
        for word in word1:
            comb1+=word
        comb2=""
        for word in word2:
            comb2+=word
        if comb1==comb2:
            return True
        else:
            return False
        