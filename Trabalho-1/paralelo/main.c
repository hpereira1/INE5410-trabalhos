#include <stdio.h>
#include "gol.h"
#include <pthread.h>
#include "gol.c"


int main(int argc, char **argv)
{
    int size, steps;
    cell_t **prev, **next, **tmp;
    FILE *f;
    stats_t stats_step = {0, 0, 0, 0};
    stats_t stats_total = {0, 0, 0, 0};

    int n_threads = atoi(argv[2]);
    if (argc != 2)
    {
        printf("ERRO! Você deve digitar %s <nome do arquivo do tabuleiro>!\n\n", argv[0]);
        return 0;
    }
    //inicializa a barrier para n_threads
    
    if ((f = fopen(argv[1], "r")) == NULL)
    {
        printf("ERRO! O arquivo de tabuleiro '%s' não existe!\n\n", argv[1]);
        return 0;
    }

    fscanf(f, "%d %d", &size, &steps);

    if (n_threads > size) n_threads = size;
    int comeco = 0;
    thread_info thread_info[n_threads];
    int intervalo = size / n_threads;
    int remainder = size % n_threads;
    pthread_t threads[n_threads];

    for (int aux = 0; aux < n_threads; aux++){
        int fim = comeco + intervalo;
        if (remainder > 0) {
            remainder++;
            fim++;
        }
        thread_info[aux].comeco = comeco;
        thread_info[aux].fim = fim;
        comeco = fim;
    }
    
    prev = allocate_board(size);
    next = allocate_board(size);

    read_file(f, prev, size);

    fclose(f);

#ifdef DEBUG
    printf("Initial:\n");
    print_board(prev, size);
    print_stats(stats_step);
#endif

    for (int i = 0; i < steps; i++)
    {
        pthread_create(&threads[i], NULL, play, (void *) &thread_info[i]);
        stats_total.borns += stats_step.borns;
        stats_total.survivals += stats_step.survivals;
        stats_total.loneliness += stats_step.loneliness;
        stats_total.overcrowding += stats_step.overcrowding;

#ifdef DEBUG
        printf("Step %d ----------\n", i + 1);
        print_board(next, size);
        print_stats(stats_step);
#endif
        tmp = next;
        next = prev;
        prev = tmp;
    }

#ifdef RESULT
    printf("Final:\n");
    print_board(prev, size);
    print_stats(stats_total);
#endif

    free_board(prev, size);
    free_board(next, size);
}
