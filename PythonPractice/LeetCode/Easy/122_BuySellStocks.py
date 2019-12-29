def maxProfit(prices):
    if(not prices):
        return 0
    maxProfit = 0
    buyPoint = 0
    N = len(prices)
    for i in range(1,N):
        if(prices[i] < prices[i-1]):
            maxProfit += (prices[i-1]-prices[buyPoint])
            buyPoint = i
    maxProfit += (prices[N-1]-prices[buyPoint])
    
    return maxProfit

prices = [3,7,1,2,5,8,3,9,2,1]
print(maxProfit(prices))