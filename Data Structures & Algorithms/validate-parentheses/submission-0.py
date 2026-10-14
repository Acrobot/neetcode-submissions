class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for token in s:
            if token in closing:
                if not stack or stack[-1] != closing[token]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(token)

        return not stack

