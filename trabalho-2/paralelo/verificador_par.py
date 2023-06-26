


def validate_sudoku(matrizes_proc, n_threads,i,inicio_index):
    index_aux = list(enumerate(matrizes_proc))
    for i, matriz_proc in index_aux:
        contador_erros=0
        print(f"Processo {i+1}: resolvendo quebra-cabeças {inicio_index + i +1}") 

        col_error = ""
        row_error = ""
        block_error = ""
    threads=[] 
    for t in range(n_threads):
        
    if contador_erros == 0:
        print(f"Processo {i+1}: {contador_erros} erros encontrados ")
    else:
        print(f"Processo {i+1}: {contador_erros} erros encontrados (T1:{row_error},{col_error},{block_error})")
 

def validate_column(matriz_proc):        
    for col in range(9):
        column = [matriz_proc[row][col] for row in range(9)]
        if len(set(column)) != 9:
            col_error += f" C{col + 1}"
            contador_erros+=1


def validate_row(matriz_proc): 
    for row_index, row in enumerate(matriz_proc):
        if len(set(row)) != 9:
            row_error += f" L{row_index + 1}"
            contador_erros+=1

def validate_block(matriz_proc):    
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):                        
            block = []
            region_row = block_row // 3  
            region_col = block_col // 3  
            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    block.append(matriz_proc[row][col])
            if len(set(block)) != 9:
                block_error += f" R{region_col + region_row * 3 + 1} "
                contador_erros+=1
    #print(f"{col_error} + {row_error} + {block_error}")



#validate vai instaciar as threads e as thread exucutarao as subfunçoes acima