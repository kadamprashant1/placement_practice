
#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

def max_profit(prices):
    minSofar=prices[0]
    max_prof=0
    for i in prices:
        minSofar= min(minSofar,i)
        profit=i-minSofar
        max_prof= max(max_prof,profit)
    return max_prof

if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    print(f"max profit is {max_profit(prices)}")