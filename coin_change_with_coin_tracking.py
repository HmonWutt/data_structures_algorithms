def coin_change(amount,coin_set):
    tracked_coins = {}
    optimal_combination = {}
    for amt in range(0,amount+1):
        optimal_combination[amt] = float("inf")
        tracked_coins[amt] = []
    
    optimal_combination[0] = 0
    for coin in coin_set:
        coins_used = []
        for amt in range(coin,amount+1):
            if optimal_combination[amt]> (1+ optimal_combination[amt-coin]):
                optimal_combination[amt] = (1+ optimal_combination[amt-coin])
                coins_used = [coin]+tracked_coins[amt-coin]
                tracked_coins[amt] = coins_used
                coins_used=[]
    return optimal_combination[amt]

            

coin_change(5,[1,3,5])
    

