# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

ways = 0

def getWay(total, coins):
  if (total == 0):
    global ways
    ways += 1
    return
  for index, coin in enumerate(coins):
    if (total >= coin):
      newTotal = total - coin
      getWay(newTotal, coins[index:])
      
getWay(200, [200, 100, 50, 20, 10, 5, 2, 1])
print(ways) # 73682

# Correct 