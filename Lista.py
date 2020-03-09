class Nodo:
  def __init__(self, dato, enlace=None):
    self.dato = dato
    self.enlace = enlace

  def agregarEnlace(self, datoN):
    self.enlace = Nodo(datoN)

  def siguiente(self):
    return self.enlace

class Lista:
  def __init__(self):
    self.primero = None
    self.ultimo = None
    self.cant =0
  def leerPrimero(self):
    return self.primero

  def inicializarLista(self, dato):
    nuevo = Nodo(dato)
    self.primero = nuevo
    self.ultimo = nuevo
    self.cant = 1

  def insertarComienzo(self, dato):
    if(self.cant>0):
      nuevo = Nodo(dato)
      nuevo.enlace = self.primero
      self.primero = nuevo
      self.cant+=1
      return self
    else:
      self.inicializarLista(dato)
  def insertarFinal(self, dato):
    if(self.cant>0):
      nuevo = Nodo(dato)
      self.ultimo.enlace = nuevo
      self.ultimo = self.ultimo.enlace
    else:
      self.inicializarLista(dato)
  def buscarLista(self, dato):
    indice=self.primero
    while(indice!=None):
      if(dato == indice.dato):
        return indice
      indice = indice.enlace
    return None
  def eliminar(self, dato):
    actual = self.primero
    anterior = None
    encontrado = False
    while((actual!=None) and actual.dato!=dato):
      if(actual.dato !=dato):
        anterior = actual
        actual = actual.enlace
    if(actual!=None):
      if(actual==self.primero):
        self.primero = actual.enlace
      else: 
        anterior.enlace = actual.enlace
      actual = None
  def visualizar(self):
    n = self.primero
    while(n!=None):
      print(str(n.dato))
      n = n.enlace

