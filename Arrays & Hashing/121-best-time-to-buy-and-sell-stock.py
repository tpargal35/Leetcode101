def maxProfit(prices: List[int]) -> int:
    low = float('inf')  # Track the lowest price seen so far (potential buy day)
    maxx = 0           # Track the maximum profit found so far
    
    for st in prices:
        if st < low:
            # Greedy step: If we find a lower price, update buy day
            low = st
        else:    
            # If current price is higher than 'low', calculate potential profit
            # and update 'maxx' if this profit is better than before
            maxx = max(maxx, st - low)
            
    return maxx

prices = [7, 1, 5, 3, 6, 4]
print(f"Max Profit: {maxProfit(prices)}")
