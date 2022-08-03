array=[]
for item in range(0,5):
    a=int(input("enter a value"))
    array.append(a) 
print(array)  
b=input("enter a element add")
array.append(b)
print(array)
position=int(input("enter add value postion"))
element=int(input("enter lemetn value"))
tep=0
for item in range(0,6):
    if item==position:
        temp=array[item]
        array[item]=element
        tep=1
    if tep!=0:
        a=arr
print(array)