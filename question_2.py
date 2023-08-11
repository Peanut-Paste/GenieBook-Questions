# Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
# Suppose we could access yesterday's stock prices as a list, where:
# • The indices are the time in minutes past trade opening time, which was 9:30am local time.
# • The values are the price in dollars of Apple stock at that time.
# So if the stock:
# cost $300 at 09:30am, stock_prices_yesterday[0] = 300
# cost $350 at 09:40am, stock_prices_yesterday[10] = 350
# cost $500 at 10:30am, stock_prices_yesterday[60] = 500

def get_max_profit(arrays):
    lowest, res = 0, 0
    for i in arrays:
        if lowest != 0 and i - lowest > res:
            res = i - lowest
        if lowest == 0 or i < lowest:
            lowest = i
    return res
            



stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 4, 6]
print(get_max_profit(stock_prices_yesterday))
# returns 6 (buying for $5 and selling for $11)