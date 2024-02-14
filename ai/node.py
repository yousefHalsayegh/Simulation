class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):

        if self.data :
            if data < self.data:
                if self.left is None:
                    self.left = Node(data) 
                else : 
                    self.left.insert_node(data)
            else: 
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data
