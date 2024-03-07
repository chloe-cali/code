import math

def findLastBinary(s):
    nums = []
      
    l,nums=[],[]
    for i in s:
        l.append(ord(i))
    for i in l:
        nums.append(int(bin(i)[2:]))
    
    count = 0 
    while count < len(nums):
        nums[count] = str(nums[count]) 
        count = count + 1
        
    
    nums = "".join(nums)


    bc = [0]
    
    cnt1 = 0
    while cnt1 < len(nums):
        

        count = 0 
        while count < len(bc):
            bc[count] = str(bc[count]) 
            count = count + 1
        

        
        bc = "".join(bc)
        nums = "".join(nums)

        result1 = nums.find(bc)
        if result1 == -1:
            break
        
        count = 0

        print(nums)                                 #fart
        print(result1)                              #fart


        nums = list(nums)

        print(nums)                                 #fart
        print(result1)                              #fart
        print(bc)                              #fart
        while count < len(bc):
            nums.pop(result1)
            print(nums)
            count = count + 1
        

        nums.reverse()
        
        bc = list(bc)

        bc.reverse()
        

        nums = "".join(nums)
        bc = "".join(bc)
        
        result2 = nums.find(bc)
        if result2 == -1:
            break
        
        nums = list(nums)
        bc = list(bc)

        count = 0
        while count <= len(bc):
            nums.pop(result2)
            count = count + 1
        
        nums.reverse()
        bc.reverse()
        
        count = 0 
        while count < len(bc):
            bc[count] = int(bc[count]) 
            count = count + 1
        
        if bc[(len(bc) - 1)] == 0:
            bc[(len(bc) - 1)] = 1
        elif bc[(len(bc) - 1)] == 1:
            bc.append(0)

        cnt1 = cnt1 + 1
    
    print(bc)

    count = 0 


    final = int(bc,2)
    print(final)
        
def main():
    s = input("enter:\n")
    findLastBinary(s)    
        
    
if __name__ == '__main__':
    main()