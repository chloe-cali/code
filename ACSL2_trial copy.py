import math

def findLastBinary(s):
     
    l,nums=[],[]
    for i in s:
        l.append(ord(i))
    for i in l:
       
        eight = str(bin(i)[2:])
       
        eight = list(eight)
       
        if len(eight) < 8:
            while len(eight)<8:
                eight.insert(0,'0')
       
        eight = "".join(eight)
       
        nums.append(eight)
   
    bc = [0]
   
    cnt1 = 0
    while cnt1 < len(nums):
       
        if type(bc) != list:
            bc = list(bc)

        count = 0
        while count < len(bc):
            bc[count] = str(bc[count])
            count = count + 1

        nums = "".join(nums)
        bc = "".join(bc)

        result1 = nums.find(bc)
       
        nums = list(nums)
        nums.reverse()
        bc = list(bc)
        bc.reverse()

        nums = "".join(nums)
        bc = "".join(bc)
       
        result2 = nums.find(bc)
       
        if (result1 == -1) and (result2 == -1):
           
            bc = list(bc)
            bc.reverse()
            bc = "".join(bc)
            bc = int(bc,2)
            bc = bc - 1
            bc = bin(bc).replace("0b","")
           
            break

        nums = list(nums)

        if result2 != -1:
            count = 0
            while count < len(bc):
                del nums[result2]
                count = count + 1

        nums = list(nums)
        nums.reverse()
        bc = list(bc)
        bc.reverse()

        if result1 != -1:
            count = 0
            while count < len(bc):
                del nums[result1]
                count = count + 1
        
        print("".join(nums))

        bc = "".join(bc)
       
        if bc == '0':
            bc = int(bc)
            bc = bc + 1
            bc = str(bc)
       
        else:
            bc = str(bc)
            bc = int(bc,2) #b to d
            bc = bc + 1
            bc = bin(bc).replace("0b","") #d to b
        cnt1 = cnt1 + 1
       
       
    if (type(bc) != str) and (type(bc) != int):
        count = 0
        while count < len(bc):
                bc[count] = str(bc[count])
                count = count + 1
    bc = "".join(bc)


    final = int(bc,2)
    print(final)
        
def main():
    s = "A is Alpha; B is Bravo; C is Charlie."
    findLastBinary(s)    
        
    
if __name__ == '__main__':
    main()