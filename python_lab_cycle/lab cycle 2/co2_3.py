#MARTIN ABRAHAM
#21MCA030
list1=[]
n=int(input("enter limit"))
print("enter numbers")
for i in range(0,n):
    data=int(input())
    list1.append(data)
print(list1)
data1=0
for x in list1:
    data1=data1+x
print(data1)
