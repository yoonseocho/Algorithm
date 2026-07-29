class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()

        for i in range(1, amount+1):
            min_coin = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min_coin = min(min_coin, dp[diff] + 1)
            dp[i] = min_coin
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
                