# Convert Ternary Expression to Binary Tree
GFG problem

Given a string that contains ternary expressions. The expressions may be nested. You need to convert the given ternary expression to a binary Tree and return the root.

Example 1:

Input: a?b:c
Output: a b c
Explanation:
string expression = a?b:c
So the binary tree for the above expression is:
       a  
     /   \   
    b     c
Example 2:

Input: a?b?c:d:e
Output: a b c d e
Explanation:
string expression =  a?b?c:d:e
So the binary tree for the above expression is:
                  a
                /   \
               b     e
             /   \
            c     d
 

Your Task:
This is a function problem, you don't need to read input/output. Just complete the function convertExpression() that take string and index(initialized from 0) as parameters and returns the root node of the binary tree

Constraints:
1 <= T <= 100
1 <= |String| <= 100