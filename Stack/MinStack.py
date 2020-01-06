#https://leetcode.com/problems/min-stack/
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Solution: Using extra stack to store min data

"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        curMin = x
        if self.minData and self.minData[-1] < curMin:
            curMin = self.minData[-1]
            
        self.minData.append(curMin)

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.data.pop()
            self.minData.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if not self.data:
            return None
        
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minData:
            return None
        
        return self.minData[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()