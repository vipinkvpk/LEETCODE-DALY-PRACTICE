import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        result = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char * -freq)
        return ''.join(result)
        