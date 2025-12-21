from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    buy = prices[0]
    max_profit = 0
    
    for i in range(1,len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        max_profit = max(prices[i] - buy, max_profit)

    return max_profit

if __name__ == "__main__":
	arr = [3,7,8,2,6,13,1,2,4,3,10]
	print(maxProfit(arr))