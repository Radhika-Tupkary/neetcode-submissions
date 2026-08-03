class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            # I am choosing nums[i] as part of my current combination. Let's keep going and see if this leads to a valid sum.
            dfs(i, cur, total + nums[i])    
            cur.pop()
            # I've explored all combinations that use nums[i]. Now let's explore combinations that never use it.
            dfs(i+1, cur, total) 

        dfs(0, [], 0)
        return res