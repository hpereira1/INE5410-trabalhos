def validate_sudoku(matrizes_proc, n_threads):
    for matriz_proc in matrizes_proc:
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
