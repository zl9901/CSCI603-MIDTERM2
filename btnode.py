"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""

class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = 'val', 'left', 'right'

    def __init__(self, val, left=None, right=None):
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right


def testBTNode():
    """
    A test function for BTNode.
    :return: None
    """
    lchild = BTNode(10)
    rchild = BTNode(20)
    parentnode = BTNode(30)
    parentnode.left = lchild
    parentnode.right = rchild
    print('parentnode value is:', parentnode.val)
    print('leftchild value is :', parentnode.left.val)
    print('rightchild value is:', parentnode.right.val)

if __name__ == '__main__':
    testBTNode()