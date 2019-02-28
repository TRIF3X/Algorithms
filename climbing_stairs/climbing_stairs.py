#!/usr/bin/python
# init

import sys

def climbing_stairs(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache is None:
    cache = {i: 0 for i in range(n+1)}
  elif cache[n] >= 1: 
    return cache[n]
  
  cache[n] = climbing_stairs(n - 1, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 3, cache)

  return cache[n]




print(climbing_stairs(4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')