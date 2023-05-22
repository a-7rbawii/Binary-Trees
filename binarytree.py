class node():
    def __init__(self, leftpointer, data, rightpointer):
        self.__lp = leftpointer
        self.__data = data
        self.__rp = rightpointer

myTree = [node for i in range(8)]
rootPointer = -1
nullPointer = -1
nextFree = 0

def findNode(myTree, item, rootpointer, nullpointer):
    found = False
    itemPointer = rootPointer

    while (myTree[itemPointer].data != item) and (itemPointer != nullPointer):
        if myTree[itemPointer].data > item:
            itemPointer = myTree[itemPointer].leftPointer
        else:
            itemPointer = myTree[itemPointer].rightPointer
    return itemPointer #if -1 then not found

def addNode(myTree, item):
    global rootPointer, nextFree
    if nextFree <= len(myTree):
        myTree[nextFree].leftPointer = -1
        myTree[nextFree].data = item
        myTree[nextFree].rightPointer = -1

        if rootPointer == -1:
            rootPointer = 0
        else:
            placed = False
            currentNode = rootPointer

            while placed == False:
                
                if myTree[currentNode].data > item:
                    if myTree[currentNode].leftPointer == -1:
                        myTree[currentNode].leftPointer == nextFree
                        placed = True
                    else:
                        currentNode = myTree[currentNode].leftPointer
                else:
                    if myTree[currentNode].rightPointer == -1:
                        myTree[currentNode].rightPointer == nextFree
                        placed = True
                    else:
                        currentNode = myTree[currentNode].rightPointer
        nextFree = nextFree + 1
    else:
        print("Tree Full")
    return myTree, rootPointer, nextFree

def preOrder(pointer):
    currentPointer = pointer
    print(myTree[currentPointer].data)

    if myTree[currentPointer].leftPointer != nullPointer:
        preOrder(myTree[currentPointer].leftPointer)
    
    if myTree[currentPointer].rightPointer != nullPointer:
        preOrder(myTree[currentPointer].rightPointer)

def inOrder(pointer):
    currentPointer = pointer
    if myTree[currentPointer].leftPointer != nullPointer:
        inOrder(myTree[currentPointer].leftPointer)
    
    print(myTree[currentPointer].data)

    if myTree[currentPointer].rightPointer != nullPointer:
        inOrder(myTree[currentPointer].rightPointer)
