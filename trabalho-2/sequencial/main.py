import sys
import time
from verificador import Verificador

args = sys.argv
matriz = []
nun_args = len(args)

file_name = args[1]
if nun_args != 4:
  print("Numero de argumentos invalidos!")
  exit()
n_process = int(args[2])
n_threads = int(args[3])

if(n_process < 1 ):
  raise Exception("ERRO! Numero de processos menor ou igual a zero")
if(n_threads < 1 ):
  raise Exception("ERRO! Numero de threads menor ou igual a zero")
#print(type(args[1]), type(args[2]),type(args[3]))
try:
    with open(file_name, 'r') as file:
      for line in file:
        line = line.strip()  # Remover espaços em branco no início e no fim da linha
        if not line:
          continue
        elements = line.split()  # Dividir a linha em elementos
        elements_int=[]
        for i in elements[0]:
          elements_int.append(int(i))
        # Adicionar os elementos à matriz
        matriz.append(elements_int)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")

#divide em x matrizes 
matrizes=[]
nova_matriz=[]
for i in matriz:
  nova_matriz.append(i)
  if len(nova_matriz)==9:
    matrizes.append(nova_matriz)
    nova_matriz=[]

t0 = time.time()
v1 = Verificador(matrizes, 1)
v1.validate_sudoku()
t1 = time.time()
print(t1-t0)


