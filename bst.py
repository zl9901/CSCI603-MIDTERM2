__author__ = 'Zhuo Liu'
from btnode import BTNode

class BST:

    __slots__ = 'root', 'size', 'variable1', 'variable2',"count"

    def __init__(self):
        self.root = None
        self.size = 0
        self.variable1 = ''
        self.variable2 = ''
        self.count=0

    def __insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = BTNode(val)
            else:
                self.__insert(val, node.left)
        else:
            if node.right is None:
                node.right = BTNode(val)
            else:
                self.__insert(val, node.right)

    def insert(self, val):
        self.variable1 += str(val)
        if self.root is None:
            self.root = BTNode(val)
        else:
            self.__insert(val, self.root)
        self.size += 1

    def __inorder(self, node):
        if node is None:
            return ' '
        else:
            return self.__inorder(node.left) + \
                   str(node.val) + \
                   self.__inorder(node.right)

    def __str__(self):
        return self.__inorder(self.root)


    def printAddedOrder(self):
        print('first_three_added_order: ',end="")
        for index1 in range(3):
            print(self.variable1[index1], end = ' ')


    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val<val:
            return self.searchBST(root.right,val)
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return root

    def bubbleSort(self,arr):
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        return arr

    def printAdded(self,root,value):
        print(str(self.searchBST(root,value).val)+"\t",end="")


    def __printValueOrder(self, node):
        if node is None:
            return ' '
        else:
            self.__printValueOrder(node.left)
            self.variable2 += str(node.val)
            self.__printValueOrder(node.right)

    def printValueOrder(self):
        print('first_three_value_order: ',end="")
        self.__printValueOrder(self.root)
        for index2 in range(3):
            print(self.variable2[index2], end = ' ')


def main():
    bst = BST()
    to_add = [5,3,6,2,7,1]
    for i in range(0,len(to_add)-1):
        bst.insert(to_add[i])
    print('list inserted into binary search tree: ', to_add)
    bst.printAddedOrder()
    print()
    bst.printValueOrder()
    value1=to_add[0]
    value2=to_add[1]
    value3=to_add[2]
    print()
    print("first_three_added_order:",end="")
    bst.printAdded(bst.root,value1)
    bst.printAdded(bst.root, value2)
    bst.printAdded(bst.root, value3)
    print()
    print("first_three_value_order:", end="")
    arr=bst.bubbleSort(to_add)
    print()
    value4 = arr[0]
    value5 = arr[1]
    value6 = arr[2]
    print(value4)
    print(value5)
    print(value6)
    
    bst.printAdded(bst.root, value4)
    bst.printAdded(bst.root, value5)
    bst.printAdded(bst.root, value6)
    print()


if __name__ == '__main__':
    main()




