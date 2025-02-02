# Another brute force solution, using enumerate

class Solution:
    def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                if num1 + num2 == target:
                    return [i, j]
        return []