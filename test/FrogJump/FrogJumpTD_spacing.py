# Top down solution with different spacing

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        target = stones[-1]

        @cache
        def dp(stone, k):
            if stone == target:
                return True
            if stone in stone_set:
                if k > 1:
                    if dp(stone + k - 1, k - 1):
                        return True
                if dp(stone + k, k):
                    return True
                if stone != 0:
                    if dp(stone + k + 1, k + 1):
                        return True
            return False

        return dp(0, 1)
