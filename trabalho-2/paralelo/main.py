import sys
import time
from multiprocessing import Process
from threading import Thread
from verificador_par import validate_sudoku

args = sys.argv
matriz = []
nun_args = len(args)

file_name = args[1]
if nun_args != 4:
  print("Numero de argumentos invalidos!")
  exit()
n_process = int(args[2])
n_threads = int(args[3])
process = []
if(n_process < 1 ):
  raise Exception("ERRO! Numero de processos menor ou igual a zero")
if(n_threads < 1 ):
  raise Exception("ERRO! Numero de threads menor ou igual a zero")
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
    exit()
#divide em x matrizes 
matrizes=[]
nova_matriz=[]
for i in matriz:
  nova_matriz.append(i)
  if len(nova_matriz)==9:
    matrizes.append(nova_matriz)
    nova_matriz=[]
    
matrizes_processos = []

tabuleiros = len(matrizes)
if ( n_process > tabuleiros):
  n_process = tabuleiros
  
inicio = 0 
fim = 0
x = 0
intervalo = tabuleiros // n_process
resto = tabuleiros % n_process
inf_proc = []

for i in range(n_process):
  inicio = inicio
  fim  += intervalo
  if resto > 0:
    resto-=1
    fim+=1
  inf_proc.append(fim)
  inicio = fim
for i in inf_proc:
  aux = []
  for e in range(x, i):
    aux.append(matrizes[e])
  matrizes_processos.append(aux)
  x=i
  
# print(inf_proc)
# print(len(matrizes_processos))
process = []
t0 = time.time()
for i in range(n_process):
    p = Process(target=validate_sudoku, args=(matrizes_processos[i],n_threads,i))
    p.start()
    process.append(p)

for p in process:
    p.join()

t1 = time.time()
print(t1-t0)


