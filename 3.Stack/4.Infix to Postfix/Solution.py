#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        stack = []
        output = ""
        prec = {'^':1,'/':2,'*':2,'+':3,'-':3,'(':4}
        for e in exp:
            if e == '+' or e == '-' or e == '*' or e == '/' or e == '^':
                if len(stack) == 0:
                    stack.append(e)
                else:
                    flag = True
                    while(flag):
                        if len(stack) != 0:
                            top = stack[-1]
                            if prec[top] > prec[e]:
                                stack.append(e)
                                flag = False
                            else:
                                output += stack.pop()
                        else:
                            stack.append(e)
                            flag = False
            
            elif e == ')':
                temp = stack.pop()
                while temp != '(':
                    output += temp
                    if len(stack) != 0:
                        temp = stack.pop()
                    else:
                        break
                    
            else:
                if e == '(':
                    stack.append(e)
                else:
                    output += e
                
        if len(stack) != 0:
            while(len(stack)!= 0):
                output += stack.pop()
                
        return output

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends