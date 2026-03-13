class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # count = 0
        # for word in allowed:
        #     word1  = word.split()
        #     for word2 in word1:
        #         if word2 in allowed:
        #             count += 1
        #     # if word in words:
        #     #     count += 1 
        # return count
        allowed= set(allowed)
        count =0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count +=1 
                    break 
        return len(words)-count



        