class NodoCola:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class ColaLista:
  def __init__(self):
    self.frente = self.fin = None
  def insertar(self, dato):
    nuevo = NodoCola(dato)
    if self.cola_vacia():
      self.frente = nuevo
    else: 
      self.fin.siguiente = nuevo
    self.fin = nuevo
  def quitar(self):
    if not self.cola_vacia():
      aux = self.frente.dato
      self.frente = self.frente.siguiente
    else:
      raise Exception("No se puede eliminar de una cola vacia")
    return aux
  def borrarCola(self):
    while(not self.frente == None):
      self.frente = self.frente.siguiente
  def frente_cola(self):
    if self.cola_vacia():
      raise Exception("Error: Cola vacia")
    return self.frente.dato
  def cola_vacia(self):
    return self.frente == None
  def visualizar(self):
    n = self.frente
    while n!=None:
      print(str(n.dato))
      n = n.siguiente