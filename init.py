class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.enlaces = []

  def agregarEnlace(self, datoN):
    self.enlaces.append(Nodo(datoN))

  def agregarEnlace(self, datoN, peso):
    self.enlaces.append(Enlace(Nodo(datoN), peso))

class Enlace:
  
  def __init__(self, nodo, peso):
    self.nodo = nodo
    self.peso = peso


n = Nodo(2)

n.agregarEnlace(3,3)

n.agregarEnlace(4,1)

print("Enlaces de " + str(n.dato) + ":\n")

for x in range(len(n.enlaces)):
  print("Enlace #" + str(x) + ": "+ str(n.enlaces[x].nodo.dato))