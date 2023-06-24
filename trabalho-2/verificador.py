def checar_numero(matriz, coluna, linha, num):
    # checa linha
    for i in range(9):
        if matriz[linha][i] == num:
            return False

    # checa coluna
    for i in range(9):
        if matriz[i][coluna] == num:
            return False

    # checa quadrado 3x3
    start_row = (linha // 3) * 3
    start_col = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if matriz[start_row + i][start_col + j] == num:
                return False
    print("foi")
    return True
