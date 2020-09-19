def maxProfit(prices):
	if(not prices):
		return 0

	N = len(prices)
	maxProfit = 0
	bp = prices[0]

	for i in range(1,N):
		if(bp <= prices[i]):
			profit = prices[i] - bp
			if(profit > maxProfit):
				maxProfit = profit
		else:
			bp = prices[i]

	return maxProfit

prices = [2,12,12,1,14]
print(maxProfit(prices))


