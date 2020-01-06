#https://leetcode.com/problems/walls-and-gates/

"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  """

"""
Optimal solution: 
Using BFS but each gate is not fully searched before moving on to a new gate. 
Each gate only looks at the areas within 1 space before we check the next gate. 
So each area within one space of the gates are checked for rooms and these rooms are marked, 
then added to the queue. Once all gates are checked, each new space is checked, and so forth. 
So, once a room gets hit, it has to be from the closest gate.
"""

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        EMPTY = 2147483647
        GATE = 0

        q = deque()
        dirs = [[0, -1], [0 , 1], [-1, 0], [1, 0]]
        m = len(rooms)
        n = len(rooms[0])

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for d in dirs:
                r2, c2 = r + d[0], c + d[1]
                if r2 < 0 or r2 == m or c2 < 0 or c2 == n or rooms[r2][c2] != EMPTY:
                    continue
                rooms[r2][c2] = rooms[r][c] + 1
                q.append((r2, c2))

        return rooms
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

rooms = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]

print(Solution().wallsAndGates(rooms))