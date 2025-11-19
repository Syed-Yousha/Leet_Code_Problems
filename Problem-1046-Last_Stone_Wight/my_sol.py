class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] 
        heapq.heapify(stones)
        
        while(len(stones)>1):
            l1 = -heapq.heappop(stones)
            l2 = -heapq.heappop(stones)
            if l1 != l2:
                new_stone = l1 - l2
                heapq.heappush(stones, -new_stone)


        return -stones[0] if stones else 0
            

#Time Complexity: O(n log n)
#Space Complexity: O(n)

#its an optimal solution