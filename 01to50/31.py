# Made by Micha de Groot

import numpy as np

def coinPerms(coins, amount, nrCoins, solutions):

    for i in range(nrCoins + 1):
        solutions[i,0] = 1

    for i in range(1, nrCoins + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                solutions[i,j] = solutions[i - 1][j] + \
                                 solutions[i][j - coins[i - 1]]

            else:
                solutions[i,j] = solutions[i - 1][j]

    print("Number of possible ways for change: %d"%solutions[-1][-1])

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 200
    nrCoins = 8
    solutions = np.zeros((nrCoins + 1, amount + 1))

    solutions = coinPerms(coins, amount, nrCoins, solutions)

main()
