from stack import Stack


def is_balanced(input_str):
    if len(input_str)%2!=0:
        return False
    else: 
        stack1=Stack()
        for i in input_str:
            if i=='(':
                stack1.push(i)
            else:
                holder=stack1.pop()
                if(holder==None):
                    return False
        if(stack1.peek()==None):
            return True
        else: 
            return False




             #in O(n) time finds out if an array of parantheses are balanced
             # the basic principle is that if ( then we owe one so we push it to the stack
             # if ) then we pop because we match them together without pushing a ) into the stack
             # This finds the condition of balancing or not using the stack 
             # Very interesting
             # I had to use Boots to figure out this question using the stack
             # will be important to revisit for review later on just to better understand the material 
             # Once I figured out the owing part it became signficantly clearer
             # THANKS BOOTS   
           