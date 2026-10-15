class Solution:
    def isValid(self, s: str) -> bool:
        closing_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in closing_pairs:
                if not stack or stack[-1] != closing_pairs[char]:
                    return False
                
                stack.pop()
            else:
                stack.append(char)

        return not stack
        