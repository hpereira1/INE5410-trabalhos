
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include "gol.h"
//#include "gol.c" 

int main(int argc, char **argv)
{
    int size, steps;
    cell_t **prev, **next, **tmp;
    FILE *f;
    stats_t stats_step = {0, 0, 0, 0};
    stats_t stats_total = {0, 0, 0, 0};

    if (argc != 3)
    {
        printf("ERRO! Você deve digitar %s <nome do arquivo do tabuleiro>!\n\n", argv[0]);
        return 0;
    }
    
    if ((f = fopen(argv[1], "r")) == NULL)
    {
        printf("ERRO! O arquivo de tabuleiro '%s' não existe!\n\n", argv[1]);
        return 0;
    }

    fscanf(f, "%d %d", &size, &steps);
    
    prev = allocate_board(size);
    next = allocate_board(size);

    int n_threads = atoi(argv[2]);
    if (n_threads > size) n_threads = size;
    int comeco = 0;


    thread_info thread_infos[n_threads];
    int intervalo = size / n_threads;
    int remainder = size % n_threads;
    pthread_t threads[n_threads];

    for (int aux = 0; aux < n_threads; aux++){
        int fim = comeco + intervalo;
        if (remainder > 0) {
            remainder--;
            fim++;
        }
        thread_infos[aux].comeco = comeco;
        thread_infos[aux].fim = fim;
        thread_infos[aux].intervalo = fim - comeco;
        thread_infos[aux].tamanho = size;
        comeco = fim;
    }



    read_file(f, prev, size);

    fclose(f);

#ifdef DEBUG
    printf("Initial:\n");
    print_board(prev, size);
    print_stats(stats_step);
#endif

    for (int i = 0; i < steps; i++)
    {
        stats_step.borns = 0;
        stats_step.loneliness = 0;
        stats_step.overcrowding = 0;
        stats_step.survivals = 0;

        for (int aux = 0; aux < n_threads; aux++) {
            thread_infos[aux].board = prev;
            thread_infos[aux].newboard = next;
            thread_infos[aux].stats_thread = stats_step;
            pthread_create(&threads[aux], NULL, play, (void *) &thread_infos[aux]);
        }
        for (int aux = 0; aux < n_threads; aux ++) {
            pthread_join(threads[aux], NULL);
            stats_total.borns += thread_infos[aux].stats_thread.borns;
            stats_total.survivals += thread_infos[aux].stats_thread.survivals;
            stats_total.loneliness += thread_infos[aux].stats_thread.loneliness;
            stats_total.overcrowding += thread_infos[aux].stats_thread.overcrowding;
        }
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
