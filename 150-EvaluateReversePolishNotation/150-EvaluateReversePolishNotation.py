class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for op in tokens:
            if op in "+-*/":
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if op == '+':
                    stack.append(operand1 + operand2)
                elif op == '-':
                    stack.append(operand1 - operand2)
                elif  op == '/':
                    stack.append(operand1 / operand2)
                else:
                    stack.append(operand1 * operand2) 

            else:
                stack.append(int(op))

        return int(stack.pop())
