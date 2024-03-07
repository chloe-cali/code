# Complete the 'findHandSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER originalRows
#  2. STRING handTiles
#  3. STRING drawPile
#

def count(lst, x):
    cnt = 0
    for ele in lst:
        if (ele == x):
            cnt = cnt + 1
    return cnt




def hand(originalRows, handTiles, drawPile):

    end = 0
    while end != 1:
        counter1 = 0
        while counter1 < len(originalRows):
            count0 = count(handTiles, originalRows[0])
            count1 = count(handTiles, originalRows[1])
            count2 = count(handTiles, originalRows[2])
            count3 = count(handTiles, originalRows[3])

            if len(handTiles) == 0:
                return originalRows, handTiles, drawPile

            if count(handTiles, originalRows[counter1]) == 0:
                if (count0 == 0) and (count1 == 0) and (count2 == 0) and (count3 == 0):
                    if len(drawPile) != 0:
                        drawPile = "".join(drawPile)
                        originalRows = "".join(originalRows)
                        find0 = drawPile.find(originalRows[0])
                        find1 = drawPile.find(originalRows[1])
                        find2 = drawPile.find(originalRows[2])
                        find3 = drawPile.find(originalRows[3])
                        drawPile = list(drawPile)
                        originalRows = list(originalRows)


                        if (find0 == -1) and (find1 == -1) and (find2 == -1) and (find3 == -1):
                            counter2 = 0
                            while counter2 < len(drawPile):
                                handTiles.append(drawPile[counter2])
                                counter2 = counter2 + 1
                            return originalRows, handTiles, drawPile
                        else:
                            if find0 == -1:
                                find0 = 999999999
                            if find1 == -1:
                                find1 = 999999999
                            if find2 == -1:
                                find2 = 999999999
                            if find3 == -1:
                                find3 = 999999999

                            drawer = min(find0, find1, find2, find3)

                            if (drawer % 2) == 0:
                                counter3 = 0
                                while counter3 <= (drawer + 1):
                                    handTiles.append(drawPile[counter3])
                                    counter3 = counter3 + 1
                            elif (drawer % 2) != 0:
                                counter3 = 0
                                while counter3 <= (drawer):
                                    handTiles.append(drawPile[counter3])
                                    counter3 = counter3 + 1
                            
                            handTiles = "".join(handTiles)
                            originalRows = "".join(originalRows)
                            finder = handTiles.find(originalRows[counter1])
                            handTiles = list(handTiles)
                            originalRows = list(originalRows)
                            if finder != -1:
                                if (finder % 2) == 0: #even
                                    tileholder = [handTiles[finder],handTiles[(finder+1)]]
                                    handTiles.pop(finder)
                                    handTiles.pop(finder)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                                elif (finder % 2) != 0: #odd
                                    tileholder = [handTiles[finder],handTiles[(finder-1)]]
                                    handTiles.pop(finder - 1)
                                    handTiles.pop(finder - 1)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                            elif finder == -1:
                                counter1 = counter1 + 1
                    else:
                        return originalRows, handTiles, drawPile
                else:
                    counter1 = counter1 + 1

            else:    
                handTiles = "".join(handTiles)
                originalRows = "".join(originalRows)
                finder = handTiles.find(originalRows[counter1])
                handTiles = list(handTiles)
                originalRows = list(originalRows)


                if finder != -1:
                    if (finder % 2) == 0: #even
                        tileholder = [handTiles[finder],handTiles[(finder+1)]]

                        if tileholder[0] == tileholder[1]: #double
                            handTiles = "".join(handTiles)
                            finder2 = handTiles.find(tileholder[1])
                            handTiles = list(handTiles)
                            if finder2 != -1:
                                if (finder2 % 2) == 0: #even
                                    handTiles.pop(finder2)
                                    handTiles.pop(finder2)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                                elif (finder2 % 2) != 0: #odd
                                    handTiles.pop(finder2 - 1)
                                    handTiles.pop(finder2 - 1)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                            else: 
                                drawPile = "".join(drawPile)
                                originalRows = "".join(originalRows)
                                find = drawPile.find(originalRows[counter1])
                                drawPile = list(drawPile)
                                originalRows = list(originalRows)
                                if find == -1:
                                    counter4 = 0
                                    while counter4 < len(drawPile):
                                        handTiles.append(drawPile[counter4])
                                        counter4 = counter4 + 1
                                    return originalRows, handTiles, drawPile
                                else: 
                                    if (find % 2) == 0:
                                        counter4 = 0
                                        while counter4 <= (find + 1):
                                            handTiles.append(drawPile[counter4])
                                            counter4 = counter4 + 1
                                    elif (find % 2) != 0:
                                        counter4 = 0
                                        while counter4 <= (find):
                                            handTiles.append(drawPile[counter4])
                                            counter4 = counter4 + 1
                                counter1 = counter1 + 1
                        else:    
                            handTiles.pop(finder)
                            handTiles.pop(finder)
                            originalRows[counter1] = tileholder[1]
                            counter1 = counter1 + 1
                    elif (finder % 2) != 0: #odd
                        tileholder = [handTiles[finder],handTiles[(finder-1)]]
                        if tileholder[0] == tileholder[1]: #double
                            handTiles = "".join(handTiles)
                            finder2 = handTiles.find(tileholder[1])
                            handTiles = list(handTiles)
                            if finder2 != -1:
                                if (finder2 % 2) == 0: #even
                                    handTiles.pop(finder2)
                                    handTiles.pop(finder2)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                                elif (finder2 % 2) != 0: #odd
                                    handTiles.pop(finder2 - 1)
                                    handTiles.pop(finder2 - 1)
                                    originalRows[counter1] = tileholder[1]
                                    counter1 = counter1 + 1
                            else: 
                                drawPile = "".join(drawPile)
                                originalRows = "".join(originalRows)
                                find = drawPile.find(originalRows[counter1])
                                drawPile = list(drawPile)
                                originalRows = list(originalRows)
                                if find == -1:
                                    counter4 = 0
                                    while counter4 < len(drawPile):
                                        handTiles.append(drawPile[counter4])
                                        counter4 = counter4 + 1
                                    return originalRows, handTiles, drawPile
                                else: 
                                    if (find % 2) == 0:
                                        counter4 = 0
                                        while counter4 <= (find + 1):
                                            handTiles.append(drawPile[counter4])
                                            counter4 = counter4 + 1
                                    elif (find % 2) != 0:
                                        counter4 = 0
                                        while counter4 <= (find):
                                            handTiles.append(drawPile[counter4])
                                            counter4 = counter4 + 1
                                counter1 = counter1 + 1
                        else: 
                            handTiles.pop(finder - 1)
                            handTiles.pop(finder - 1)
                            originalRows[counter1] = tileholder[1]
                            counter1 = counter1 + 1
                elif finder == -1:
                    counter1 = counter1 + 1










def findHandSum(originalRows, handTiles, drawPile):
    originalRows = str(originalRows)
    if len(originalRows) < 4:
        while len(originalRows) < 4:
            originalRows = "0" + originalRows
    originalRows = list(originalRows)

    handTiles = handTiles.replace(" ","")
    handTiles = list(handTiles)

    drawPile = drawPile.replace(" ","")
    drawPile = list(drawPile)

    originalRows, handTiles, drawPile = hand(originalRows, handTiles, drawPile)

    handTiles = int(handTiles)
    final = sum(handTiles)
    print(final)


                


    
    




def main():

    x = findHandSum(5923, "56 27 73 34 99 45 32 17 64 57 18 11", "36 92 22 50 82")
    print(x)

if __name__ == '__main__':
    main()