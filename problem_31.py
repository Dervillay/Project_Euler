# Target amount we want to make
target = 200

# Value in pence of coins available
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# For each n up to target, store number of ways to make up that value
ways = [0 for x in range(target+1)]
ways[0] = 1

# Dynamic programming approach that considers increasing groups
# of the coins available for all value up to target
for i in range(len(coins)):
    for j in range(coins[i], target+1):
        ways[j] += ways[j - coins[i]]

print(ways[target])





