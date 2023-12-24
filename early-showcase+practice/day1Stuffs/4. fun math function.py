# fun math function
import math

def mat(op,num1,num2):
    if op == 0:
        result = num1+num2
    elif op == 1:
        result = num1-num2
    elif op == 2:
        result = num1*num2
    elif op == 3:
        result = num1/num2
    elif op == 4:
        result = math.floor(num1/num2)
    else:
        print("error in mat")
        return 0
    return result

print(mat(4,1,2))
