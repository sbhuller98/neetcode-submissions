class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = -1
        
        store = {}

        def recurse(amt, coinsSoFar):
            for coin in coins:
                if amt >= coin:
                    newAmt = amt - coin
                    coinsTotal = coinsSoFar + 1
                    if newAmt in store and store[newAmt] <= coinsTotal:
                        continue
                    store[newAmt] = coinsTotal
                    if newAmt == 0:
                        nonlocal ans
                        if ans > 0:
                            ans = min(ans, coinsTotal)
                        else:
                            ans = coinsTotal
                        return
                    else:
                        recurse(newAmt, coinsTotal)
        
        recurse(amount, 0)
        return ans
                
                    
