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

    def levelorder_traversal(self):
        fila = []
        node = self.root
        fila.append(node)
        while (fila):
            if node.left:
                fila.append(node.left)
            if node.right:
                fila.append(node.right)
            try:
                node = fila[1]
            except IndexError:
                pass
            print(fila.pop(0), end=' ')


class BinarySearchTree(BinaryTree):
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
        
    def min(self, node=None):
        if not node:
            node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def max(self, node=None):
        if not node:
            node = self.root
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                aux = self.min(node.right)
                node.data = aux
                node.right = self.remove(aux, node.right)

        return node

if __name__ == "__main__":
    ftree = BinarySearchTree()
    nodes = [12, 9, 20, 3, 10, 18, 80, 1, 4, 13, 23]
    for n in nodes:
        ftree.insert(n)

    ftree.inorder_traversal()
    print('')
    ftree.postorder_traversal()
    print(f'\nAltura: {ftree.height()} nós.')
    ftree.levelorder_traversal()
    print("")
    print(f"Min:{ftree.min()} e Max:{ftree.max()}")
    ftree.remove(12)
    ftree.levelorder_traversal()