import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-el for el in nums]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []
        tempK = self.k
        while tempK > 1:
            el = heapq.heappop(self.heap)
            temp.append(el)
            tempK -= 1

        result = heapq.heappop(self.heap)
        heapq.heappush(self.heap, result)
        
        i, n = 0, len(temp)
        while i < n:
            heapq.heappush(self.heap, temp.pop())
            i += 1

        return -result