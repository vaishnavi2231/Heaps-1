''' Time Complexity : O(nlogk) : n: no of all elements, k no of lists 
    Space Complexity : O(k) : k size heap 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

'''

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i,node in enumerate(lists): 
            if node:
                heapq.heappush(heap, (node.val, i,node))

        dummy = ListNode(-1)
        curr = dummy

        while heap:
            value, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            if curr.next:
                heapq.heappush(heap, (curr.next.val, i, curr.next))
        return dummy.next