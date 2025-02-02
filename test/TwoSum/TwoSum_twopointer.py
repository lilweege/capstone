# Two pointer solution

class Solution:
    def two_sum_two_pointers(nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted((num, i) for i, num in enumerate(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            sum_ = nums_sorted[left][0] + nums_sorted[right][0]
            if sum_ == target:
                return [nums_sorted[left][1], nums_sorted[right][1]]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        return []