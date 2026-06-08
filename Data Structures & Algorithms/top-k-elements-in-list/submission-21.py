class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        count = {}   # {num: freq}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        print(heap)

        for i in range(len(heap)): 
            element = heapq.heappop(heap)
            result.append(element[1])

        return result









    
        