#martin abraham
#21mca030

list =[]
f = open("demofile.txt" , 'r')
for x in f:
  print(x)
  list.append(x)
print("the list is ", list)
