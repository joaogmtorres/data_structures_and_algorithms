class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # insertion

    def _insert_recursive(self, current, value):
        if value < current.key:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        
        elif value > current.key:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)

    def insert (self, value):
        if not self.root:
            self.root = Node(value)
        
        else:
            self._insert_recursive(self.root, value)

    # insertion
    
    # printing

    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root

        if node.right:
            self.printTree(node.right, level+1)

        print('    ' * level + str(node.key))

        if node.left:
            self.printTree(node.left, level+1)
    
    # printing

    # searching

    def _search_recursive(self, current, value):

        if current is None:
            print(f"Number {str(value)} not found" )
            return

        elif value == current.key:
            print(f"{str(value)} Found on tree, you can print the tree now")
            return
        
        elif value > current.key:
            self._search_recursive(current.right, value)    

        elif value < current.key:
            self._search_recursive(current.left, value)  

    def search(self, value):
        self._search_recursive(self.root, value)    
    
    # searching

    # deleting
    
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_recursive(self, current, value):

        if current is None:
            return None

        if value > current.key:
            current.right = self._delete_recursive(current.right, value)
        
        elif value < current.key:
            current.left =  self._delete_recursive(current.left, value)

        elif current.key == value:
            if not current.left and not current.right:
                return None
            
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            elif current.left and current.right:
                successor = self.find_min(current.right)
                current.key = successor.key
                current.right = self._delete_recursive(current.right, successor.key)

        return current
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    # deleting

test = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for i in values:
    test.insert(i)

test.search(30)
test.search(10)

test.printTree()