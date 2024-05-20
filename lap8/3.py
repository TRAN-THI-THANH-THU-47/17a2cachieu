def cubesum(n):
    
    return sum(int(digit)**3 for digit in str(n))

def isArmstrong(n):

    return n == cubesum(n)

def PrintArmstrong():
    
    for i in range(1, 1000):
        if isArmstrong(i):
            print(i)

print("cubesum(123):", cubesum(123))  

print("isArmstrong(153):", isArmstrong(153))  
print("isArmstrong(123):", isArmstrong(123))  


PrintArmstrong()
 
