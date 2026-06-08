class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1:1, 2:2, 3:3, 5:3, 7:3}

        # {frequency: [num1, num2, num3]}

        if len(set(nums)) == k:
            return list(set(nums))
        
        num_to_count_dict = {}
        count_to_num_dict = {}

        for num in nums:
            if num in num_to_count_dict:
                num_to_count_dict[num] += 1
            else:
                num_to_count_dict[num] = 1

        print(num_to_count_dict)

        for num in num_to_count_dict:
            frequency = num_to_count_dict[num]
            if frequency in count_to_num_dict:
                count_to_num_dict[frequency].append(num)
            else:
                count_to_num_dict[frequency] = [num]

        print(count_to_num_dict)

        frequency_count = sorted(list(count_to_num_dict.keys()))
        print(frequency_count)
        result = []

        for freq in reversed(frequency_count[-k:]):
            if len(result) == k:
                break
            result.extend(count_to_num_dict[freq])


        return result




    
        