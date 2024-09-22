arraynodes = [(0) * 3 for x in range (20)] # ARRAY[0;19][0;2] OF INTEGER
                                         # d efining 2d array for defining rows we use for x in range no of rows
rootpointer = -1
freenode = 0
def addnode(arraynodes,rootpointer,freenode):
    #by ref when used in qs we return the values as python doesnot have it
    #and returning it makes it by ref hence we can also retun
    #multiple values
    nodedata = int(input("enter the data ="))
    if freenode <= 19 :
        arraynodes[freenode][0] = -1
        arraynodes[freenode][1] = nodedata
        arraynodes[freenode][2] = -1
        if rootpointer == -1:
            rootpointer = 0
        else:
            placed = False
            currentnode = rootpointer
            while placed ==False:
                if nodedata < arraynodes[currentnode][1]:
                    if arraynodes [currentnode][0] == -1:
                        arraynodes[currentnode][0] = freenode
                        placed = True
                    else:
                        currentnode = arraynodes[currentnode][0]
                else:
                    if arraynodes[currentnode][2] == -1:
                        arraynodes[currentnode][2] = freenode
                        placed = True
                    else:
                        currentnode = arraynodes[currentnode][2]
        freenode = freenode + 1
    else:
        print("tree is full")
    return arraynodes,rootpointer,freenode

#c
def printall(arraynodes):
    for x in range (20) :
        print(str(arraynodes[x][0])), " ", str(arraynodes[x][1] ,
                                              " ",str(arraynodes[x][2]))

for x in range(10):
    arraynodes,rootpointer,freenode = addnode(arraynodes,rootpointer,freenode)
    #returning values in and storing  seqence
printall(arraynodes)

