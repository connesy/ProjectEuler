# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def coin_combinations(total_pennies: int, coins: list[int]) -> list[list[int]]:
    """Return the number of unique ways to make up the total number of pennies given a list of coin values"""
    if total_pennies == 0:
        return [[]]

    combinations: list[list[int]] = []
    for coin in coins:
        if coin <= total_pennies:
            lower_coins = COINS[COINS.index(coin) :]  # Coins with same or lower denomination than coin
            combinations_of_rest = coin_combinations(total_pennies - coin, coins=lower_coins)
            combinations.extend([[coin, *combination] for combination in combinations_of_rest])

    return combinations


if __name__ == "__main__":
    combinations = coin_combinations(total_pennies=200, coins=COINS)
    print(combinations)
    print()
    print("Combinations: ", len(combinations))
