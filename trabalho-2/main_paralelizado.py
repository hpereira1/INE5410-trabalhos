import sys
import time
from verificador import checar_numero
from multiprocessing import Process
from threading import Thread
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

#abaixo, caso tabuleiros/process seja par sera dividido homogeneamente, caso contrario tera o resto separado entre os processos
tabuleiros=matriz/9
if tabuleiros % n_process == 0:
    tabuleiros_divididos=[]
    tabuleiros_por_processo = tabuleiros // n_process
    matrizes = []
    nova_matriz = []
    for i in matriz:
        nova_matriz.append(i)
        if len(nova_matriz) == 9:
            matrizes.append(nova_matriz)
            nova_matriz = []
            if len(matrizes) == tabuleiros_por_processo:
                tabuleiros_divididos.append(matrizes)
                matrizes = []
else:
    tabuleiros_divididos=[]
    tabuleiros_por_processo = tabuleiros // n_process
    resto = tabuleiros % n_process
    matrizes = []
    nova_matriz = []
    for i in matriz:
        nova_matriz.append(i)
        if len(nova_matriz) == 9:
            matrizes.append(nova_matriz)
            nova_matriz = []
            if len(matrizes) == tabuleiros_por_processo:
                if resto > 0:
                    tabuleiros_divididos.append(matrizes)
                    matrizes = []
                    resto -= 1
                else:
                    tabuleiros_divididos[-1].extend(matrizes)
                    matrizes = []


#nao tenho certeza, mas imagino que aqui seriam as funcoes que os processos precisam tratar, dai daqui dentro a gnt aplicaria as threads 
def funcao_processos():
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





processos=[]
for i in (0,n_process):
  proc = Process(target=funcao_processos)
  proc.start()
  processos.append(proc)

for i in processos:
   i.join()
'''



'''
#processos devem dividir o trabalho
#threads sao para correcao