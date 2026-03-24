class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        total_count = Counter()
        for word in words:
            total_count += Counter(word)
        n=len(words)
        for char in total_count:
            if total_count[char] % n != 0:
                return False 
        return True

        