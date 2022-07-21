'''
#1
def listInput():
    input_list=[]
    input_string=" "
    while True:
        input_string=input()
        if input_string =="":
            break
        input_list.append(int(input_string))
    return input_list
def listSum(input_list):
    index=1
    sum=0
    for element in input_list:
        if(index%2!=0):
            sum+=element
        index=index+1
    return sum

input_list=listInput()
sum=listSum(input_list)
print(sum)
'''
'''
import math
#2
def listInput():
    input_list=[]
    input_string=""
    while True:
        input_string=input()
        if input_string =="":
            break
        input_list.append(int(input_string))
    return input_list
def pairsComp(input_list):
    result_list=[]
    list_len=len(input_list)
    a=math.ceil(len(input_list) / 2)
    for i in range(0,a,1):
        result_list.append(input_list[i]*input_list[list_len-1-i])
    return result_list
pair_list=listInput()
pair_list=pairsComp(pair_list)

print(pair_list)
'''
'''
#3
def listInput():
    input_list=[]
    input_string=""
    while True:
        input_string=input()
        if input_string =="":
            break
        input_list.append(str(input_string))
    return input_list
def decFractionSeparate(input_list):
    end_list=[]
    for i in input_list:

      for j in range(0,len(i),1):
         if(i[j]=='.'):
             a=i[j+1:len(i)]
             if(a==''):
                 end_list.append('0')
             else:
                 end_list.append("0."+i[j+1:len(i)])
             break
    return end_list
def minMaxVar(input_list):
    max = 0
    min = float(input_list[0])
    for i in input_list:
        if(float(i)>max):
            max=float(i)
        elif(float(i)<min):
            min=float(i)
    var=max-min
    return var
dec_list=listInput()
dec_list=decFractionSeparate(dec_list)
var=minMaxVar(dec_list)
print(var)
'''
'''
#4
def convertToBinary(num):
    b = ''
    while num > 0:
        b = str(num % 2) + b
        num = num // 2
    return b
num=int(input())
print(convertToBinary(num))
'''