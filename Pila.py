class NodoPila:
  def __init__(self, elemento):
    self.elemento = elemento
    self.siguiente = None

class PilaLista:
  def __init__(self):
    self.cima = None

  def pilaVacia(self):
    return self.cima == None

  def insertar(self, elemento):
    nuevo = NodoPila(elemento)
    nuevo.siguiente = self.cima
    self.cima = nuevo
  def quitar(self):
    if(self.pilaVacia()):
      raise Exception("Pila Vacia, no se puede extraer")
    aux = self.cima.elemento
    self.cima = self.cima.siguiente
    return aux
  def cimaPila(self):
    if(self.pilaVacia()):
      raise Exception("Pila vacia, no se puede leer la cima")
    return self.cima.elemento
  def limpiarPila(self):
    t = None
    while(not self.pilaVacia()):
      t = self.cima
      self.cima = self.cima.siguiente
      t.siguiente = None
  def buscarLista(self, dato):
    indice=self.cima
    while(indice!=None):
      if(dato == indice.elemento):
        return indice
      indice = indice.siguiente
    return None
  def visualizar(self):
    n = self.cima
    while n!=None:
      print(str(n.elemento))
      n = n.siguiente