class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter 
        word_count = Counter(s1.split())+ Counter(s2.split())
        return [word for word,freq in word_count.items() if freq==1] 