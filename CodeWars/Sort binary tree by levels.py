class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def findNodes(nodes:list):
    outputnodes= []
    for node in nodes:
        if node.left or node.right:
            if node.left: outputnodes.append(node.left)
            if node.right: outputnodes.append(node.right)
    if len(outputnodes)>0: return outputnodes
    return None
    
def tree_by_levels(node: Node):
    nodes = []
    link = 0
    if node:
        nodes.append(node)
        while True:
            value= findNodes(nodes[link:])
            if value!=None:
                nodes.extend(value)
                link=len(nodes)-len(value)
            else:
                break
        return list(map(lambda x: x.value, nodes))
    else:
        return []


a = Node(Node(Node(None,None,4),None,1),Node(None,Node(None,None,5),2),3)  
print(tree_by_levels(a))