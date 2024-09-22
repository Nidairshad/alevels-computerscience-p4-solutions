QueueArray = [""]* 10 #ARRAY[0:9] OF STRING
headpointer = 0 #INTEGER
tailpointer = 0 #INTEGER
NumberOfItems = 0 #INTEGER
#if using variables in function we globalize the varirable so that its value could be used inside the function
def enqueue(QArray,headp,tailp,Numitems,datatoadd):
    #returns boolean , also parameters name are not nesscary to same with variable
    #however when calling them use the same variable like QueueArrray
    if Numitems == 10 :
        return (False,QArray,headp,tailp,Numitems) #BYREF so we return those paramters that are byref
    QArray[tailp]=datatoadd
    if tailp >=9:
        tailp = 0
    else:
        tailp = tailp + 1
    Numitems = Numitems+1
    return (True,QArray,headp,tailp,Numitems)#orginal variables values are changed/updated
def Dequeue(QArray,headp,tailp,numitems): #returns string
    if numitems == 0:
        return ("False",QArray,headp,tailp,numitems)
    itemremoved = QArray[headp]
    headp = headp + 1
    if headp >= 9:
        headp = 0
    numitems = numitems - 1
    return (itemremoved,QArray,headp,tailp,numitems)
for x in range (11):
    userinput = input("enter data item please")
    added,QueueArray,headpointer,tailpointer,NumberOfItems= enqueue(QueueArray,headpointer,tailpointer,NumberOfItems,userinput)
    #Added variable assign to false or true thing ie QueueArray
    if added == True:
        print("item added sucessfully")
    else:
        print("queue is full,item not added")
item,QueueArray,headpointer,tailpointer,NumberOfItems = Dequeue(QueueArray,headpointer,tailpointer,NumberOfItems)
print(item,"is removed")
item,QueueArray,headpointer,tailpointer,NumberOfItems = Dequeue(QueueArray,headpointer,tailpointer,NumberOfItems)
print(item,"is removed")






