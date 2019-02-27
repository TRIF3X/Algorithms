#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # create a variable to track our max profit
  max_profit = 0
  # create a variable to track our current profit
  current_profit = 0
  # loop through the prices
  # add each iteration to current_profit
  # if we go negative we will reset current_profit to 0
  # if current_profit is greater than our max_profit, our max_profit is now our current_profit
  # return max_profit

  




print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))