#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # create a variable to track our max profit
  max_profit = 0
  # create a variable to track our current profit
  current_profit = 0
  # loop through the prices
  # our current_profit will equal the price at iteration - the first item in the list
  # if current_profit is greater than our max_profit, our max_profit is now our current_profit
  # if our current_profit is less than our max_profit, our current_profit is now a loss
  # if there is no max profit we will return the loss
  # return max_profit
  while len(prices) > 0:
    for x in range(len(prices)):
      current_profit = prices[x] - prices[0]
      if current_profit > max_profit:
        max_profit = current_profit
      if current_profit < max_profit:
        loss = current_profit
    del prices[0]
  if max_profit == 0:
    return loss
  return max_profit


  




print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))