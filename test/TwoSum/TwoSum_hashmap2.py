# Variant of hash map solution

class Solution:
    def two_sum_one_pass(nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if (complement := target - num) in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []