class Node:
    def __init__(self, item, leftPointer, rightPointer):
        self.item = item
        self.leftPointer = leftPointer
        self.rightPointer = rightPointer

def nodeAdd(itemAdd):
    global nextFreePointer, rootPointer, myTree
    if nextFreePointer == nullPointer:
        print("No nodes free")
    else:
        itemAddPointer = nextFreePointer
        nextFreePointer = myTree[nextFreePointer].leftPointer
        itemPointer = rootPointer
        if itemPointer == nullPointer:
            rootPointer = itemAddPointer
        else:
            leftBranch = False
            while itemPointer != nullPointer:
                oldPointer = itemPointer
                if myTree[itemPointer].item > itemAdd:
                    leftBranch = True
                    itemPointer = myTree[itemPointer].leftPointer
                else:
                    leftBranch = False
                    itemPointer = myTree[itemPointer].rightPointer
            if leftBranch:
                myTree[oldPointer].leftPointer = itemAddPointer
            else:
                myTree[oldPointer].rightPointer = itemAddPointer
        myTree[itemAddPointer].leftPointer = nullPointer
        myTree[itemAddPointer].rightPointer = nullPointer
        myTree[itemAddPointer].item = itemAdd

def find(itemSearch):
    itemPointer = rootPointer
    while myTree[itemPointer].item != itemSearch and itemPointer != nullPointer:
        if myTree[itemPointer].item > itemSearch:
            itemPointer = myTree[itemPointer].leftPointer
        else:
            itemPointer = myTree[itemPointer].rightPointer
    return itemPointer

def menu():
    while True:
        print("Enter 1 to add a node")
        print("Enter 2 to find an item")
        print("Enter 3 to exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            itemAdd = int(input("Enter the item to add: "))
            nodeAdd(itemAdd)
        elif option == 2:
            itemSearch = int(input("Enter the item to search for: "))
            result = find(itemSearch)
            if result == -1:
                print("Item not found")
            else:
                print("Item found at index", result)
        elif option == 3:
            break
        else:
            print("Invalid option, try again")

nullPointer = -1
rootPointer = nullPointer
nextFreePointer = 0
myTree = [Node(0, i + 1, i + 1) for i in range(11)]
myTree[10].leftPointer = nullPointer

menu()