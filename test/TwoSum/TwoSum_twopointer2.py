# Another two pointer solution, calling sort differently

class Solution:
    def two_sum_two_pointers(nums: List[int], target: int) -> List[int]:
        indexed_nums = [(value, index) for index, value in enumerate(nums)]
        indexed_nums.sort()
        left, right = 0, len(indexed_nums) - 1
        while left < right:
            total = indexed_nums[left][0] + indexed_nums[right][0]
            if total == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []