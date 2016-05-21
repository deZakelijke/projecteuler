def readData():
    f = open('11.txt')
    grid = []
    i = 0
    for line in f:
        grid.append([])
        for j in range(0,60,3):
            integer = int(line[j:j+2])
            grid[i].append(integer)
        i += 1
    f.close()
    return grid

def main():
    data = readData()
    maxProduct = 0
    # loop through vertically, horizontally and diagonally twice
    for i in range(0,20):
        for j in range(0,16):
            product = data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3]
            if product > maxProduct:
                maxProduct = product
    for i in range(0,20):
        for j in range(0,16):
            product = data[j][i]*data[j+1][i]*data[j+2][i]*data[j+3][i]
            if product > maxProduct:
                maxProduct = product
    for i in range(0,16):
        for j in range(0,16):
            product = data[j][i]*data[j+1][i+1]*data[j+2][i+2]*data[j+3][i+3]
            if product > maxProduct:
                maxProduct = product
    for i in range(16,0,-1):
        for j in range(0,16):
            product = data[j][i]*data[j+1][i-1]*data[j+2][i-2]*data[j+3][i-3]
            if product > maxProduct:
                maxProduct = product



    print maxProduct

main()
