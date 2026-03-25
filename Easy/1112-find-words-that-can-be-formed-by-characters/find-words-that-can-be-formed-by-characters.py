class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        from collections import Counter 
        char_count = Counter(chars)
        total_length = 0
        for word in words:
            word_count=Counter(word)
            if all(char_count[char] >= count for char, count in word_count.items()):
                total_length += len(word)
        return total_length
            