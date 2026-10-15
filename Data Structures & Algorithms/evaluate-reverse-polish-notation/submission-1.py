class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '-': (lambda x, y: y - x),
            '+': (lambda x, y: y + x),
            '/': (lambda x, y: int(y / x)),
            '*': (lambda x, y: y * x)
        }

        stack = []
        for token in tokens:
            if token in operations:
                x, y = stack.pop(), stack.pop()
                res = operations[token](x, y)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]