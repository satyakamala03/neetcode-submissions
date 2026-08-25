# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = 0

        for lst in lists:
            if lst:
                minHeap.append((lst.val, counter, lst))
                counter += 1

        heapq.heapify(minHeap)

        head = ListNode()
        cur = head

        while minHeap:
            _, cntr, cur.next = heapq.heappop(minHeap)
            cur = cur.next
            if cur.next:
                heapq.heappush(minHeap, (cur.next.val, cntr, cur.next))
        
        return head.next
            

