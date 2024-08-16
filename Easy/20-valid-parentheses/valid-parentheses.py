class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {')':'(','}':'{',']':'['}
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if stack and stack[-1] == parentheses_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack)==0
        