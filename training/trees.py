import os

class binaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        print(self)
        self.right = right
    
    def __str__(self):
        return self.value.__str__()        
        # line = None

        # if self.left:
        #     line = str(self.left) 
            
        # if self.value:
        #     if line is None:
        #         line = str(self.value)
        #     else:
        #         line = line + ', ' + str(self.value)
            
        # if self.right:
        #     if line is None:
        #         line = str(self.right)
        #     else:
        #         line = line + ', ' + str(self.right)
                 
        # return (line)
    
      

    def __repr__(self):
        return self.__str__()      
    
    def insert(root, value):

        if isinstance(value, binaryTreeNode):
            value = value.value

        if root is None:
            return binaryTreeNode(value)
        
        if value < root.value:
            root.left = binaryTreeNode.insert(root.left, value)
        else:
            root.right = binaryTreeNode.insert(root.right, value)
        return root     


A=binaryTreeNode(10)
B=binaryTreeNode(5)
C=binaryTreeNode(15)
D=binaryTreeNode(3)
E=binaryTreeNode(7)
F=binaryTreeNode(12)

print(A)
A.insert(B)
A.insert(C)
A.insert(D)
A.insert(E)
A.insert(F)


print(A)
print(B)
print(C)    

