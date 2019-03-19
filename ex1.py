comandi="""Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """

flag=True
lista=[]
lung=0

while flag:
    num=input(comandi)
    num=int(num)
    if num==1:
        new=input("Insert new task: ")
        lista.append(new)
        lung+=1
        print("")
    elif num==2:
        old=input("Insert task to delete: ")
        lista.remove(old)
        lung-=1
        print("")
    elif num==3:
        print("Lista completa: ")
        for elem in sorted(lista):
            print(elem)
        print("")
    elif num==4:
        flag=False