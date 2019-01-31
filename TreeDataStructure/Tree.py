#           2 
#     1                3 
# null  null       null    null
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right= None
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data):
        node=Node(data)
        node.left=None
        node.right=None
        if self.root is None:
            #mean we are inserting element at root of the bst
            self.root=node
        else:
            currentNode=self.root
            while True:
                if node.data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left =node
                        break
                    currentNode=currentNode.left
                if node.data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right=node
                        break
                    currentNode=currentNode.right
    def printInorder(self):
        node=self.root
        self._inOrder(node)
    def _inOrder(self,node):
        if node:
            self._inOrder(node.left)
            print(node.data)
            self._inOrder(node.right)
tree=Tree()
tree.add(9)
tree.add(3)
tree.add(94)
tree.add(19)
tree.add(39)
tree.add(97)
tree.add(900)
tree.add(967)
tree.add(954)
tree.add(90)
tree.printInorder()



                    
