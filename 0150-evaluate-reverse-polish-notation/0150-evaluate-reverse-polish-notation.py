class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Evaluate reverse Polish notation. array of strings tokens that represents a valid arithmetic expresion. So its from orders so like brackets first then multiplication and division then subtraction and addition. We need to return the value from the total expression. So in a expression where 1,2,+ thats 1+2 we have the expression at the end and then add it for each number. So potentially I feel like we could have a stack that adds values and then stores the resulting value in the stack after popping and then we simply pop the last value left. Ok so this idea works. Its kind of an extension of the previous problem with brackets.
        valueStack = []
        operands = {"+", "-", "*", "/"}

        for v in tokens:
            if v in operands:
                v2 = valueStack.pop()
                v1 = valueStack.pop()

                if v == "+":
                    valueStack.append(v1+v2)
                elif v == "-":
                    valueStack.append(v1-v2)
                elif v == "*":
                    valueStack.append(v1*v2)
                else:
                    valueStack.append(int(v1/v2))

            else:
                valueStack.append(int(v))
        
        return valueStack.pop()
        # what is the run time? this is O(n) with O(n) Space