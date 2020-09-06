class Solution:
    """You are given an array. Each element represents the price of a stock on that particular day.
     Calculate and return the maximum profit you can make from buying and selling that stock only once."""
    @staticmethod
    def buy_and_sell(arr):
        lowest_stock_price = arr[0]
        current_profit = 0
        for p in arr:
            if p > lowest_stock_price:
                current_profit = p - lowest_stock_price
            else:
                lowest_stock_price = p

        return current_profit


if __name__ == '__main__':
    print(Solution().buy_and_sell([9, 11, 8, 5, 7, 10]))
    # 5
