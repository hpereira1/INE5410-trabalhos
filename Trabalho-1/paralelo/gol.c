/*
 * The Game of Life
 *
 * RULES:
 *  1. A cell is born, if it has exactly three neighbours.
 *  2. A cell dies of loneliness, if it has less than two neighbours.
 *  3. A cell dies of overcrowding, if it has more than three neighbours.
 *  4. A cell survives to the next generation, if it does not die of lonelines or overcrowding.
 *
 * In this version, a 2D array of ints is used.  A 1 cell is on, a 0 cell is off.
 * The game plays a number of steps (given by the input), printing to the screen each time.
 * A 'x' printed means on, space means off.
 *
 */
#include <stdlib.h>
#include <pthread.h>
#include "gol.h" // claudio


/* Statistics */


stats_t statistics;
cell_t **allocate_board(int size)
{
    cell_t **board = (cell_t **)malloc(sizeof(cell_t *) * size);
    int i;
    for (i = 0; i < size; i++)
        board[i] = (cell_t *)malloc(sizeof(cell_t) * size);
    
    statistics.borns = 0;
    statistics.survivals = 0;
    statistics.loneliness = 0;
    statistics.overcrowding = 0;

    return board;
}

void free_board(cell_t **board, int size)
{
    int i;
    for (i = 0; i < size; i++)
        free(board[i]);
    free(board);
}

int adjacent_to(cell_t **board, int size, int i, int j)
{
    int k, l, count = 0;

    int sk = (i > 0) ? i - 1 : i;
    int ek = (i + 1 < size) ? i + 1 : i;
    int sl = (j > 0) ? j - 1 : j;
    int el = (j + 1 < size) ? j + 1 : j;

    for (k = sk; k <= ek; k++)
        for (l = sl; l <= el; l++)
            count += board[k][l];
    count -= board[i][j];

    return count;
}

void *play(void *arg)
{
    unsigned int i, j, a;
    thread_info *aux = (thread_info*) arg;

    //stats_t stats = {0, 0, 0, 0};

    /* for each cell, apply the rules of Life */

    for (i = aux -> comeco; i < aux -> fim; i++)
    {
        for (j = 0; j < aux -> tamanho; j++)                   
        {
            a = adjacent_to(aux ->board,aux -> tamanho ,i, j);

            /* if cell is alive */
            if(aux ->board[i][j]) 
            {
                /* death: loneliness */
                if(a < 2) {
                    aux ->newboard[i][j] = 0;
                    aux -> stats_thread.loneliness++;
                }
                else
                {
                    /* survival */
                    if(a == 2 || a == 3)
                    {
                        aux -> newboard[i][j] = aux -> board[i][j];
                        aux -> stats_thread.survivals++;
                    }
                    else
                    {
                        /* death: overcrowding */
                        if(a > 3)
                        {
                            aux -> newboard[i][j] = 0;
                            aux -> stats_thread.overcrowding++;
                        }
                    }
                }
                
            }
            else /* if cell is dead */
            {
                if(a == 3) /* new born */
                {
                    aux -> newboard[i][j] = 1;
                    aux -> stats_thread.borns++;
                }
                else /* stay unchanged */
                    aux -> newboard[i][j] = aux -> board[i][j];
            }
    }
    }
    //pthread_exit(NULL);
    //return aux -> stats_thread;
    pthread_exit(NULL);
}

void print_board(cell_t **board, int size)
{
    int i, j;
    /* for each row */
    for (j = 0; j < size; j++)
    {
        /* print each column position... */
        for (i = 0; i < size; i++)
            printf("%c", board[i][j] ? 'x' : ' ');
        /* followed by a carriage return */
        printf("\n");
    }
}

void print_stats(stats_t stats)
{
    /* print final statistics */
    printf("Statistics:\n\tBorns..............: %u\n\tSurvivals..........: %u\n\tLoneliness deaths..: %u\n\tOvercrowding deaths: %u\n\n",
        stats.borns, stats.survivals, stats.loneliness, stats.overcrowding);
}

void read_file(FILE *f, cell_t **board, int size)
{
    char *s = (char *) malloc(size + 10);

    /* read the first new line (it will be ignored) */
    fgets(s, size + 10, f);

    /* read the life board */
    for (int j = 0; j < size; j++)
    {
        /* get a string */
        fgets(s, size + 10, f);

        /* copy the string to the life board */
        for (int i = 0; i < size; i++)
            board[i][j] = (s[i] == 'x');
    }

    free(s);
}