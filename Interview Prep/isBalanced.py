def isBalanced(s):
    # We take advantage of the concept of owing brackets to the stack we take away
    # so it maintains balancing.
    # if we take away when its not the right one then that just means its unbalanced.
    stack=[]

    for x in s:
        if x=='{' or x=='[' or x=='(':
            stack.append(x)
        elif (x==']' or x=='}' or x==')') and len(stack)==0:
            return "NO"
        elif x==']':
            if stack[len(stack)-1]=='[':
                stack.pop()
            else:
                return "NO"
        elif x==')':
            if (stack[len(stack)-1]=='('):
                stack.pop()
            else:
                return "NO"
        elif x=='}':
            if (stack[len(stack)-1]=='{'):
                stack.pop()
            else:
                return "NO"
    if len(stack)==0:
        return "YES"
    else: 
        return "NO"