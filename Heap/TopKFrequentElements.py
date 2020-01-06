#https://leetcode.com/problems/top-k-frequent-elements/

"""
Given a non-empty array of integers, return the k most frequent elements.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        dict = defaultdict(int)

        for no in nums:
            dict[no] += 1

        q = []
        for key in dict:
            heapq.heappush(q, (dict[key], key))
            if len(q) > k:
                heapq.heappop(q)

        return [v for f, v in q]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """