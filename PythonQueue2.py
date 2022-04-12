#Gianna Rao
#PythonQueueAssignment

names=[]
for x in range(0,10):
    name= input("enter name: ")
    names.append(name)
    #names.insert(0,name)
    print(names)
for x in range(0,10):
    print(names.pop(0))
print(names)
