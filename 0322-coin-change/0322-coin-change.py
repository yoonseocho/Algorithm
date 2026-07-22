class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for i in range(1, amount+1):
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                dp[i] = min(dp[i], dp[diff] + 1)
        
        return dp[amount] if dp[amount] < float('inf') else -1