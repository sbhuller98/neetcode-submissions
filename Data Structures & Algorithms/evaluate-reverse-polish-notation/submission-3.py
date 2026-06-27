class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = []
        for tok in tokens:
            match tok:
                case "+":
                    val2 = curr.pop()
                    val1 = curr.pop()
                    curr.append(val1 + val2)
                case "-":
                    val2 = curr.pop()
                    val1 = curr.pop()
                    curr.append(val1 - val2)
                case "*":
                    val2 = curr.pop()
                    val1 = curr.pop()
                    curr.append(val1 * val2)
                case "/":
                    val2 = curr.pop()
                    val1 = curr.pop()
                    curr.append(int(val1 / val2))
                case _:
                    curr.append(int(tok))
        return curr.pop()