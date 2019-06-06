#!/usr/bin/python
# a place to store the index & a place to store the value & a high and low var
# iterate over the array and grab the lowest in order and the largest in the array.
import argparse


def find_max_profit(prices):
    min_price = prices[0]

    if len(prices) < 2:
        return None
    max_profit = (prices[1] - prices[0])
    for i in range(1, len(prices) - 1):
        price = prices[i]
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price

    return max_profit


if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
