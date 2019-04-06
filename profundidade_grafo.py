class Node:
	# Construtor do nó, recebe um valor para identifica-lo, e uma lista de nós que adjacentes a ele
	def __init__(self, value, adj = list()):
		self.value   = value
		self.adj     = adj
		self.visited = False
		self.checked = False

# Algoritmo de pre ordem recursivo
def pre_order(n:Node):
	# Visita o grafo
	print(n.value)
	n.visited = True
	# Iremos visitar cada no adjacente ao atual, se ele ja nao foi visitado
	for a in n.adj:
		a.checked = True
		if not a.visited:
			pre_order(a)

def post_order(n:Node):
	n.visited = True
	# Iremos visitar cada no adjacente ao atual, se ele ja nao foi visitado
	for a in n.adj:
		if not a.visited:
			post_order(a)
	# Visita o grafo
	print(n.value)

# Cria os nos (Exemplo que o professor deu em aula)
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.adj = [b, c]
b.adj = [a, d]
c.adj = [a, d]
d.adj = [b, c]

#pre_order(a)
post_order(a)