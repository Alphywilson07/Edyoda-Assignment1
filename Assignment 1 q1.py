#fibonacci Seriesof numbers (0,1,1,2,3,5,8,13,21)

num1=0
num2=1

for i in range(1,11,1):
    print(num1)
    
    next_num=num2+num1
    num1 = num2
    num2=next_num
    
   
    