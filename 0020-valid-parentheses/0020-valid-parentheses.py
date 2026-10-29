class Solution:
    def isValid(self, s: str) -> bool:
        # valid parantheses we have a string s consisting of the following characters ( ) {} and [] the input string we need to find for validity every every open bracket is closed by the same type of close bracket. We need to maintain an ordering and every close bracket has a corresponding open bracket so their is never a free ) bracket. True if valid and false otherwise. So what approaches can we take here. Order is important. Therefore we need to keep some level of ordering. I think a rudimentary approach is taking a middle element and then expanding out and we automatically know that non even numbers are false. Otherwise we can probably take this as a stack. We loop through each element only adding left brackets and and then popping when we see the corresponding close bracket. We will always have the most recent and needing closing brackets on top and then we move progressively. if the stack is empty by the end we simply return true else if we ever reach a point where the closing bracket is not valid we early return false.
        stack = []
        if len(s)<=1:
            return False

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return True if not stack else False