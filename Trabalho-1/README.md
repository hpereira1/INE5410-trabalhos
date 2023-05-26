O Jogo da Vida (The Game of Life - GoL) é um autômato celular inventado pelo matemático John Conway da
Universidade de Cambridge (https://playgameoflife.com). Ele consiste em uma coleção de células que, baseadas
em algumas poucas regras matemáticas, podem viver, morrer ou se multiplicar. Dependendo das condições iniciais,
as células formam vários padrões durante todo o curso do jogo.
A versão do jogo adotada nesse trabalho possui um tabuleiro quadrado (matriz ou array 2D) onde as células são
atualizadas (modificadas) em cada geração (timestep) de acordo com as seguintes regras:
• Uma célula viva que possui menos de dois vizinhos vivos morre de solidão;
• Uma célula viva que possui dois ou três vizinhos vivos continua no mesmo estado para a próxima geração;
• Uma célula viva que possui mais de três vizinhos vivos morre de superpopulação;
• Uma célula morta que possui exatamente três vizinhos vivos se torna uma célula viva.
A Figura 1 mostra um exemplo de uma simulação de 7 gerações do GoL em um tabuleiro de tamanho 11x11.
Células vazias/mortas e vivas são representadas pelas cores cinza claro e escuro, respectivamente. A Figura 1a mostra
a situação inicial do tabuleiro. As Figuras 1b–1h mostram o resultado em cada uma das 7 gerações
Figura 1: Exemplo de uma simulação de 7 gerações do Game of Life em um tabuleiro de tamanho 11x11.
2 Definição do Trabalho
O trabalho da disciplina de Programação Concorrente consiste em desenvolver uma versão paralela do GoL utilizando
a biblioteca POSIX threads. As threads deverão dividir o trabalho da computação de forma a acelerar a execução
da aplicação.
Você deverá utilizar como base a versão sequencial do GoL implementada em C disponível no Moodle. Nessa versão,
os parâmetros de entrada são descritos em um arquivo texto. A primeira linha informa o tamanho do tabuleiro e o
número de gerações (ambos inteiros) separados por um espaço em branco. As linhas seguintes representam as células
do tabuleiro inicial, onde um espaço em branco representa uma célula vazia/morta e um “x“ representa uma célulaviva. As linhas do arquivo são separadas por quebras de linhas (line breaks). Como saída, o programa escreve na tela
o último tabuleiro, ou seja, após a execução de todas as gerações.
Na versão paralela, você deverá incluir um parâmetro de entrada para a execução do programa via linha de comando
(argc, argv) correspondente ao número de threads que deverão ser utilizadas na computação
