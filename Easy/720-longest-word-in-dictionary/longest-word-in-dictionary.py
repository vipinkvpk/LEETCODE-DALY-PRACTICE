class TrieNode:
    def __init__(self):
        self.children={}
        self.word=""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            node=root 
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word 
        stack = list(root.children.values())
        longest=""

        while stack:
            node = stack.pop()
            if node.word != "":
                if len(node.word) > len(longest) or \
                (len(node.word)==len(longest) and node.word <longest):
                    longest=node.word 
                stack.extend(node.children.values())
        return longest
