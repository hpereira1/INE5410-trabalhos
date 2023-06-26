n_process = 4
tabuleiros = 11

inicio = 0 
fim = 0
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
  for x in range(i):
    aux.append(matrizes[x])
  matrizes_processos.append(aux)
  i +=i
print(inf_proc)
