class Verificador:
    def __init__(self, matrizes_proc: list, n_threads):
        self.matrizes_proc = matrizes_proc
        self.threads = n_threads
        
        
    def validate_sudoku(self):
        for matriz_proc in self.matrizes_proc:
            col_error = ""
            row_error = ""
            block_error = ""
            for col in range(9):
                column = [matriz_proc[row][col] for row in range(9)]
                if len(set(column)) != 9:
                    col_error += f" C{col + 1}"
                    
            for row_index, row in enumerate(matriz_proc):
                if len(set(row)) != 9:
                    row_error += f" L{row_index + 1}"

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
                        
            print(f"{col_error} + {row_error} + {block_error}")
                    # for i in range(9):
        #     if matriz[linha][i - 1] == num:
        #         print('foi linha')

        #         return 1 ,"L"+str(i+1)

        # # verifica coluna
        # for i in range(9):
        #     if matriz[i-1][coluna] == num:
        #         print('foi coluna')

        #         return 1,"Q"+str(i+1)

        # # verifica quadrado 3x3
        # start_row = (linha // 3) * 3
        # start_col = (coluna // 3) * 3
        # for i in range(3):
        #     for j in range(3):
        #         if int(matriz[start_row + i][start_col + j]) == num:
        #             print('foi area')

        #             return 1
        # return 0
