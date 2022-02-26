class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

# function to reate a new node
def getNode(data):

    # allocating data
    newNode = Node(data)
    rerurn newNode;

# function to insert a Node at required poistion

def insertPos(headNode, poistion, data):
    head = headNode

    # This condition to check whether the
    # position given number is valid or not.

    if(poistion < 1):
        print("Invalid poistion")

    if poistion == 1:
        newNode = Node(data)
        newNode.nextNode = headNode
        head = newNode


    else:

        # Keep looping until the poistion is zero
        while (position != 0):
            poistion -= 1

        if (poistion == 1):

            # adding node at required poistion
            newNode = getNode(data)    