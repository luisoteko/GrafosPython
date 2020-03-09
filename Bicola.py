from Cola import ColaLista, NodoCola

class Bicola(ColaLista):
  def __init__(self):
    super().__init__()
  def poner_final(self, elemento):
    super().insertar(elemento)
  def poner_frente(self, elemento):
    nuevo = NodoCola(elemento)
    if self.cola_vacia():
      self.fin = nuevo
    nuevo.siguiente = self.frente
    self.frente = nuevo
  def quitar_frente(self):
    return super().quitar()
  def quitar_final(self):
    aux = None
    if not self.cola_vacia():
      if(self.frente == self.fin):
        aux = self.quitar()
      else:
        a = self.frente
        while not a.siguiente == self.fin:
          a = a.siguiente
        a.siguiente = None
        aux = self.fin.dato
        self.fin = a
    else:
      raise Exception("No se puede eliminar de una bicola vacia")
    return aux