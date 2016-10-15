# Made by Micha de Groot

def main():
    value = 200
    coins = [1,2,5,10,20,50,100,200]
    coinPerm = [1]
    for i in range(1,value+1):
        print("value: ",i)
        coinPerm.append(0)
        for coin in coins:
            if i-coin >= 0:
                print("Previous set: ", i-coin)
                print("New coin: ", coin)
                coinPerm[i] += (coinPerm[i-coin])
        print("New Set: ", coinPerm[i])
        print("-----")
    print(coinPerm)





main()

