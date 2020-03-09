from Lista import Nodo, Lista
from Pila import NodoPila, PilaLista
from Cola import NodoCola, ColaLista
from Bicola import Bicola

def ejemploLista():
  lista = Lista()

  lista.insertarFinal(2)
  lista.insertarFinal(3)
  lista.insertarFinal(4)
  lista.insertarFinal(5)
  lista.insertarComienzo(6)

  print("Busqueda: " + str(lista.buscarLista(4).dato))

  lista.visualizar()

  lista.eliminar(4)
  print("4 Eliminado")
  lista.visualizar()

def ejemploPila():
  lista = PilaLista()

  lista.insertar(2)
  lista.insertar(4)
  lista.insertar(6)

  print("Busqueda " + str(lista.buscarLista(4).elemento))
  lista.visualizar()
  print(lista.quitar())
  print(lista.quitar())
  print(lista.quitar())
  lista.visualizar()

def ejemploCola():
  lista = ColaLista()

  lista.insertar(1)
  lista.insertar(2)
  lista.insertar(3)
  lista.insertar(4)
  
  print(lista.quitar())
  print(lista.quitar())
  print(lista.quitar())
  print(lista.quitar())

def ejemploBiCola():
  lista = Bicola()

  lista.poner_final(1)
  lista.poner_final(2)
  lista.poner_frente(3)
  lista.poner_frente(4)
  
  print("-----")
  lista.visualizar()
  print("-----")
  
  print(lista.quitar_final())
  print(lista.quitar_final())
  print(lista.quitar_frente())
  print(lista.quitar_frente())

ejemploBiCola()
