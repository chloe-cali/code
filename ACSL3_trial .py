

def onlyLeftOrRight(input):
    lets = []
    nums = []
    
    input = list(input)
    
    poot = input[0] + "0"
    lets.append(poot)
    nums.append("0")
    
    cnt = 1
    
    while cnt < len(input):
        check = input[cnt] + str(cnt) 
        lets.append(check)
        lets.sort()
        
        dex = lets.index(check)
        
        if dex == 0:
            newnum = int(nums[0]) + 1
            nums.insert(0, str(newnum))
        elif dex == (len(lets) - 1):
            newnum = int(nums[(len(nums) - 2)]) + 1
            nums.append(str(newnum))
        else: 
            right = int(nums[dex - 1])
            left = int(nums[dex])
            if right > left:
                newnum = right + 1
            elif left > right:
                newnum = left + 1
            elif left == right:
                newnum = left + 1
            nums.insert(dex, str(newnum))
        
        cnt = cnt + 1
    
    first = []
    second = []

    cnt = 0

    while cnt < len(lets):
        check = lets[cnt]
        dex = lets.index(check)
        fin = str(int(nums[dex]) + 1)
        nums = "".join(nums)

        print(check)
        print(nums[dex])
        print(fin)

        if dex == 0:
            dex2 = nums.find(fin)
            if dex2 == -1:
                pass
            else: 
                nums = list(nums)
                fakenums = nums[1:]
                cnt1 = 0
                while cnt1 < int(nums[dex]):
                    fakenums = "".join(fakenums)
                    dex3 = fakenums.find(str(cnt1))
                    if dex3 < (dex2 - 1):
                        pass
                    else:
                        second.append(check)
                    cnt1 = cnt1 + 1



        elif dex == (len(lets) - 1): 
            dex2 = nums.find(fin)
            if dex2 == -1: 
                pass
            else:
                nums = list(nums)
                fakenums = nums[:1]
                cnt1 = 0
                while cnt1 < int(nums[dex]):
                    fakenums = "".join(fakenums)
                    dex3 = fakenums.find(str(cnt1))
                    if dex3 > (dex2 - 1):
                        pass
                    else:
                        first.append(check)
                    cnt1 = cnt1 + 1


        else:
            stringer1 = 0
            stringer2 = 0
            dex2 = nums.find(fin)
            if dex2 == -1: 
                pass
            else: 
                fakenums = list(nums)
                del(fakenums[dex2])
                fakenums = "".join(fakenums)
                dex3 = fakenums.find(fin)
                if dex3 == -1: 
                    if dex2 > dex:
                        nums = list(nums)
                        lside = nums[dex:]
                        lside = "".join(lside)

                        cnt1 = 0
                        while cnt1 < int(nums[dex]):
                            dex4 = lside.find(str(cnt1))
                            if int(dex4) < dex2:
                                pass
                            else: 
                                stringer1 = stringer1 + 1 
                                
                                rside = nums[:dex]
                                rside = "".join(rside)
                                cnt2 = 0
                            while cnt2 < int(nums[dex]):
                                dex4 = rside.find(str(cnt1))
                                if int(dex4) > dex2:
                                    pass
                            else:
                                stringer1 = stringer1 + 1

                            cnt1 = cnt1 + 1

                    elif dex2 < dex:
                        nums = list(nums)
                        rside = nums[:dex]
                        rside = "".join(rside)
                              
                        cnt1 = 0
                        while cnt1 < int(nums[dex]):
                            dex4 = rside.find(str(cnt1))
                            if int(dex4) < dex2:
                                pass
                        else:
                            stringer2 = stringer2 + 1

                        
                    if stringer1 == 1 and stringer2 == 0:
                        first.append(check)
                    elif stringer2 == 1 and stringer1 == 0:
                        second.append(check)
                    else: 
                        pass


        cnt = cnt + 1
    
    #NOY H

    print(first)
    print(" ")
    print(second)



def main():
    s = input("enter:\n")
    onlyLeftOrRight(s)    
    
    
if __name__ == '__main__':
    main()