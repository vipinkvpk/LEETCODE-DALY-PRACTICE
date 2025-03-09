class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         # for word in word1:
#         #     comb1="".join(word1)

#         # for word in word2:
#         #     comb2="".join(word2)
        combined_string_1 = ""
        for individual_word in word1:
            combined_string_1 += individual_word

        combined_string_2 = ""
        for individual_word in word2:
            combined_string_2 += individual_word

        return combined_string_1 == combined_string_2




# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         return "".join(word1)=="".join(word2)

        
        