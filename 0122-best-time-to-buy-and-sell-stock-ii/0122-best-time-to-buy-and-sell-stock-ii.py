class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        total_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            if price - min_price > max_profit:
                # print(f"{price} - {min_price} = {price - min_price}")
                max_profit = max(price - min_price, max_profit)
                min_price = price
                total_profit += max_profit
                max_profit = 0
        return total_profit