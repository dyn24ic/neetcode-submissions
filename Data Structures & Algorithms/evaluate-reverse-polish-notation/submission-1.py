class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for t in tokens:
            match t:
                case "+":
                    n2 = stack.pop()
                    n1 = stack.pop()
                    res = n1 + n2
                    stack.append(res)
                case "-":
                    n2 = stack.pop()
                    n1 = stack.pop()
                    res = n1 - n2
                    stack.append(res)
                case "*":
                    n2 = stack.pop()
                    n1 = stack.pop()
                    res = n1 * n2
                    stack.append(res)
                case "/":
                    n2 = stack.pop()
                    n1 = stack.pop()
                    res = int(n1 / n2)
                    stack.append(res)
                case _:
                    stack.append(int(t))
        
        return stack.pop()