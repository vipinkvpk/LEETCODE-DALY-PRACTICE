class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res= []
        for i,word1 in enumerate(words):
            is_substring = False
            for j, word2 in enumerate(words):
                if i!=j:
                    if word1 in word2:
                        
                        is_substring = True
                        break 

            if is_substring:
                res.append(word1)
        return res
    
        