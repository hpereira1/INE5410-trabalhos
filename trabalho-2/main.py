import sys
import time
from verificador import checar_numero

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
        
        # Adicionar os elementos à matriz
        matriz.append(elements)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
'''if matriz is not None:
  for row in matriz:
    print(row)'''
#print(len(matriz))

#divide em 4 matrizes
matrizes=[]
nova_matriz=[]
for i in matriz:
  nova_matriz.append(i)
  if len(nova_matriz)==9:
    matrizes.append(nova_matriz)
    nova_matriz=[]

#sequencial 
inicio = time.time()
for tabuleiro in matrizes:
  for linhas in tabuleiro:
    for num in linhas: 
      checar_numero(tabuleiro,linhas.index(num),tabuleiro.index(linhas),num)
      
fim = time.time()
tempo_execucao = fim - inicio
print(inicio)
print(fim)
print(tempo_execucao)