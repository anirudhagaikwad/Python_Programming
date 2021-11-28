class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left child: ' + str(self.left) + ', Right child: ' + str(self.right))

tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
print(tree)