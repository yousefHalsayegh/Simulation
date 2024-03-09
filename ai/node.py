import graphviz
class Node:
    count = 0
    def __init__(self, data):
        self.children = []
        self.data = data
        self.id = Node.count
        self.dot = graphviz.Digraph('tree', format = "png") 
        Node.count += 1

    def insert_node(self, data):

        if len(self.children) < 5:
            self.children.append(Node(data))
        else:
            for i in self.children:
                if len(i.children) > 4:
                    continue
                i.insert_node(data)
                return
                


    def render_tree(self):
        self.dot.node(f'{self.id}', label= f'{self.data}')
        for i in range(len(self.children)):
            self.dot.node(f'{self.children[i].id}', label = f'{self.children[i].data}')
            self.dot.edge(f'{self.id}', f'{self.children[i].id}', constraint='true')
                
            
        print(self)
            
        
        

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'