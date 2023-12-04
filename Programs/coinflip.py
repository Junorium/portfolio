import random

# args: amount of flips
def coin_flip(trials):
  results = []
  if isinstance(trials, int):
    for i in range(trials):
      results.append(randint(0, 1))
  else:
    return -1

# test case
prit(coin_flip(10))
    
