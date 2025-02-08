class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        if not strs:
            return ""
        
        # Let's assume the first word is the longest common prefix
        prefix = strs[0]
        
        # Compare the prefix with the rest of the words
        for word in strs[1:]:
            # Keep shrinking the prefix until it matches
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove the last character
                if not prefix:
                    return ""
        
        return prefix
