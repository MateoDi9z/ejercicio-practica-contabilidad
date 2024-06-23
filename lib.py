file_in = "datos/in.txt"
file_out = "datos/out.txt"

def crear_nuevo_ingreso(id: str, sender: str, amount: int):
  """Crea un nuevo registro de ingreso utilizando los argumentos

  Args:
      id (str): Example -> "10"
      sender (str): Example -> "Mateo"
      amount (int): Example -> "1000"
  """
  
  f = open(file_in, "a")
  f.write(f"{id}-{sender}-{amount}\n")
  f.close()

def crear_nuevo_egreso(id: str, receiver: str, amount: int):
  """Crea un nuevo registro de egreso utilizando los argumentos

  Args:
      id (str): Example -> "10"
      receiver (str): Example -> "Mateo"
      amount (int): Example -> "1000"
  """

  f = open(file_out, "a")
  f.write(f"{id}-{receiver}-{amount}\n")
  f.close()

def ingresos() -> dict:
  """ Devuelve un diccionario cuyas keys son nombres y sus values son
      una lista que representa los ingresos que este realizo """
  
  temp = dict()
  f = open(file_in, "r")
  registros = f.read().strip().split("\n")

  if len(registros) < 2: return temp

  for registro in registros:
    id, sender, amount = tuple(registro.split("-"))
    if sender not in temp.keys():
      temp[sender] = []
    temp[sender].append((id, sender, amount))

  return temp

def gastos() -> dict:
  """ Devuelve un diccionario cuyas keys son nombres y sus values son
      una lista que representa los gastos realizados a cada destino """
  
  temp = dict()
  f = open(file_out, "r")
  registros = f.read().strip().split("\n")

  if len(registros) < 2: return temp

  for registro in registros:
    id, receiver, amount = tuple(registro.split("-"))
    if receiver not in temp.keys():
      temp[receiver] = []
    temp[receiver].append((id, receiver, amount))

  return temp


def clear_ingresos():
  """ Limpia todos los registros de ingresos
  """

  f = open(file_in, "w")
  f.write("")
  f.close()

def clear_gastos():
  """ Limpia todos los registros de gastos
  """

  f = open(file_out, "w")
  f.write("")
  f.close()


# Ejemplos

## Crear registros
crear_nuevo_ingreso("1", "Mateo", 100)
crear_nuevo_egreso("1", "Mateo", 50)

# Ver registros
print(ingresos())
print(gastos())

# Borrar registros
clear_ingresos()
clear_gastos()