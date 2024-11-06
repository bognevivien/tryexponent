from typing import List


def coin_change(amount: int, coins: List[int])-> int:
    dp =[amount+1 for _ in range(amount+1)]
    print(dp, len(dp))
    dp[0]  = 0
    for a in range(1, amount+1):
        for c in coins:
            if a-c >= 0:
                dp[a] = min(dp[a], 1+ dp[a-c])
    
    return dp[amount]



amount = 11
coins = [1, 2, 5]
print(coin_change(amount, coins))