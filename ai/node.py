import graphviz
class Node:

    def __init__(self, data):
        self.children = []
        self.data = data
        self.dot = graphviz.Digraph('tree') 

    def insert_node(self, data):

        if len(self.children) < 5:
            self.children.append(Node(data))
        else:
            for i in self.children:
                i.insert_node(data)


    def render_tree(self):
        self.dot.node(f'{self.data}')
        for i in range(len(self.children)):
            self.dot.node(f'{self.data}')
            self.dot.edge(f'{self.data}', f'{i}', constraint='false')
            
            
        


    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'