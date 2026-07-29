class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort()

        for i in range(1, amount+1):
            min_coin = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min_coin = min(min_coin, dp[diff] + 1)
            dp[i] = min_coin
        
        print(dp)

        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1