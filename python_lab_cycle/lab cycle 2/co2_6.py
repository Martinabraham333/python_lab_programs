#MARTIN ABRAHAM
#21MCA030
s=str(input("enter string"))
dict={}
for i in s:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)