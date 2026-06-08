class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        # count = {}   # {num: freq}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # heap = []
        # for num in count:
        #     heapq.heappush(heap, (count[num], num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # result = []

        # for i in range(k): 
        #     result.append(heapq.heappop(heap)[1])

        # return result

        # Bucket sort
        count = {}   # {num: freq}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [0] * (len(nums)+1)
        print(freq)
        print(count)
        for num in count:
            if freq[count[num]] == 0:
                freq[count[num]] = [num]
            else:
                
                freq[count[num]].append(num)
        print(freq)

        result = []
        for el in reversed(freq):
            if el != 0:
                result.extend(el)
            if len(result) == k:
                break

        return result









    
        