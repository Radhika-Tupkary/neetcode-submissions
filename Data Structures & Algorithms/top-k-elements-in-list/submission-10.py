class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        num_to_count_dict = {}

        for num in nums:
            num_to_count_dict[num] = num_to_count_dict.get(num, 0) + 1
        

        return sorted(num_to_count_dict, key=num_to_count_dict.get, reverse=True)[:k]








    
        