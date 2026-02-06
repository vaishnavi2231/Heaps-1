# SOlution 1 : Brute Force
''' Time Complexity : O(nlogn) 
    Space Complexity : O(1) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : sort the array and take n - k element
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        return nums[n-k]

# SOlution 2 : USing Min heap of size k
''' Time Complexity : O(nlog k) 
    Space Complexity : O(k) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : if len of heap is greater than k ; pop the min element
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# SOlution 2 : USing Max heap of size n - k
''' Time Complexity : O(nlog(n-k)) 
    Space Complexity : O(n-k) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : Create heap of size n - k: means k elements would be outside of heap.
              push and pop the elements and maintain result to save the min element.
              
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        result = float("inf")
        size = n - k
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
            if len(heap) > size:
                ele = heapq.heappop(heap)
                result = min(result, -ele)
        return result