class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)
    

class BinaryTree:
    def __init__(self, Node=None):
        self.root = Node

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            elif value > x.data:
                x = x.right
            else:
                break
        if parent == None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        elif value > parent.data:
            parent.right = Node(value)

    def inorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left is not None:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right is not None:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')

    def height(self, node=None):
        if not node:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hleft > hright:
            return hleft + 1
        return hright + 1
    
    def search(self, value):
        return self._search(value, self.root)
    
    def _search(self, value, node):
        if node == None:
            return None
        if node.data == value:
            return BinaryTree(node)
        elif value < node.data:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def levelorder_traversal(self):
        aux = {}
        if self.root is None:
            return None
        aux.append(self.root)


if __name__ == "__main__":
    ftree = BinaryTree()
    ftree.insert(10)
    ftree.insert(1)
    ftree.insert(3)
    ftree.insert(80)
    ftree.insert(23)
    ftree.insert(18)
    ftree.insert(13)
    ftree.insert(9)
    ftree.insert(12)

    ftree.inorder_traversal()
    print('')
    ftree.postorder_traversal()
    print(f'\nAltura: {ftree.height()} nós.')