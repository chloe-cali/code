# Complete the 'findHandSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER originalRows
#  2. STRING handTiles
#  3. STRING drawPile
#


def main():
    fart = [1,2,3,4]

    end = 0
    while end != 1:
        counter1 = 0
        while counter1 < len(fart):
            fart[counter1] = fart[counter1] + 1
            if fart [counter1] == 10:
                end = 1
                print(fart[counter1])
                break
            else:
                print(fart[counter1])
                counter1 = counter1 + 1
    
    x = "56 27 73 34 99 45 32 17 64 57 18 11"
    x = x.replace(" ","")
    print(x)
    x = list(x)
    print(x)
    x = "".join(x)
    print(x)
                              

if __name__ == '__main__':
    main()