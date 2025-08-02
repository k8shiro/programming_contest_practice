class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

root = Node("root")
child1 = Node("child1")
child2 = Node("child2")
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node("child1.1"))