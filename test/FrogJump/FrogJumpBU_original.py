# Bottom up solution

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(1)
        
        for stone in stones:
            for k in dp[stone]:
                next_stone = stone + k
                if next_stone in stone_positions:
                    if next_stone == stones[-1]:
                        return True
                    if k - 1 > 0:
                        dp[next_stone].add(k - 1)
                    dp[next_stone].add(k)
                    dp[next_stone].add(k + 1)
        
        return False