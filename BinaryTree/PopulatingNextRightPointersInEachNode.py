#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

#Solution 1: BFS travel tree by levels -> O(n)

#Solution 2:
We only move on to the level N+1 when we are done establishing the next pointers for the level N.
Since we have access to all the nodes on a particular level via the next pointers, 
we can use these next pointers to establish the connections for the next level or the level containing their children.
         

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution(object):
    #O(1) solution
    def connect(self, root):
        if not root:
            return None
        leftMost = root
        node = leftMost
        while leftMost.left:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
                node = node.next
            else:
                leftMost = leftMost.left
                node = leftMost
        
        return root
    
    #My O(n) solution
    """
    def connect(self, root):
        if not root:
            return None
        
        q = deque([root])
        while q:
            prev = None
            count = len(q)
            for i in range(count): 
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            prev = None
        return root
        """
    
        """
        :type root: Node
        :rtype: Node
        """
