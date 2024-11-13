from anytree import Node, RenderTree, PreOrderIter, PostOrderIter, LevelOrderIter
import matplotlib.pyplot as plt
import networkx as nx

# Crear el árbol binario de 5 niveles
root = Node("0")
# Nivel 2
a = Node("1", parent=root)
b = Node("2", parent=root)
# Nivel 3
c = Node("3", parent=a)
d = Node("4", parent=a)
e = Node("5", parent=b)
f = Node("6", parent=b)
# Nivel 4
g = Node("7", parent=c)
h = Node("8", parent=c)
i = Node("9", parent=d)
j = Node("10", parent=d)
k = Node("11", parent=e)
l = Node("12", parent=e)
m = Node("13", parent=f)
n = Node("14", parent=f)
# Nivel 5
o = Node("15", parent=g)
p = Node("16", parent=g)
q = Node("17", parent=h)
r = Node("18", parent=h)
s = Node("19", parent=i)
t = Node("20", parent=i)
u = Node("21", parent=j)
v = Node("22", parent=j)
w = Node("23", parent=k)
x = Node("24", parent=k)
y = Node("25", parent=l)
z = Node("26", parent=l)
aa = Node("27", parent=m)
ab = Node("28", parent=m)
ac = Node("29", parent=n)
ad = Node("30", parent=n)

# Mostrar el árbol en texto plano en la consola
for pre, _, node in RenderTree(root):
    print(f"{pre}({node.name})")

# Crear un grafo de NetworkX
G = nx.DiGraph()

# Agregar nodos y aristas al grafo
for node in PreOrderIter(root):
    if node.parent:
        G.add_edge(node.parent.name, node.name)

# Función para la posición jerárquica
def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}
    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5,
                       pos=None, parent=None, parsed=[]):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children) != 0:
            dx = width / len(children) 
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root, parsed=parsed)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

# Dibujar el árbol
plt.figure(figsize=(12, 10))
pos = hierarchy_pos(G, root=root.name)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=False)
plt.title("Visualización del Árbol Binario de 5 Niveles")
plt.show()

# Recorridos del árbol

# Nivel-orden (amplitud)
level_order = [f"({node.name})" for node in LevelOrderIter(root)]
print("Recorrido Nivel-orden:", level_order)

# Preorden
preorder = [f"({node.name})" for node in PreOrderIter(root)]
print("Recorrido Preorden:", preorder)

# Postorden
postorder = [f"({node.name})" for node in PostOrderIter(root)]
print("Recorrido Postorden:", postorder)

# Inorden (definido manualmente)
def inorder_traversal(node):
    if node is None or node.is_leaf:
        return [f"({node.name})"] if node else []
    result = []
    if node.children:
        result += inorder_traversal(node.children[0])
    result.append(f"({node.name})")
    if len(node.children) > 1:
        result += inorder_traversal(node.children[1])
    return result

print("Recorrido Inorden:", inorder_traversal(root))
