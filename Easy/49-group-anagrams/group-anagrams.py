from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups=defaultdict(list)

        for str in strs:
            sorted_key="".join(sorted(str))
            anagram_groups[sorted_key].append(str)
        return list(anagram_groups.values())
        