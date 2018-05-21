## QUESTÃO 4 ##
#
# Você foi solicitado a escrever um programa para classificar tuplas (nome, idade, altura)
# por ordem crescente, em que nome é uma string, idade e altura são números. As tuplas
# são inseridas pelo console. O critério de classificação é:
#
# 1: Ordenar com base no nome;
# 2: Em seguida, classifique com base na idade;
# 3: Em seguida, classifique por pontuação.
#
# A prioridade é essa nome > idade > pontuação.
#
# Se as seguintes tuplas são dadas como entrada para o programa:
# Tom 19,80
# João, 20,90
# Jony, 17,91
# Jony, 17,93
# Json, 21,85
#
# Então, a saída do programa deve ser:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21 ',' 85 '), (' Tom ',' 19 ',' 80 ')]
#
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado.
# A saída deve ser impressa no formato apresentado acima.
# Valores inválidos (fora do formato esperado para uma tupla) devem ser descartados.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    tuple_list = []
    user_input = input().split(',')
    while(user_input != ['']):
        tuple_list.append(tuple(user_input))
        user_input = input().split(',')
    tuple_list.sort()
    print(tuple_list)


if __name__ == '__main__':
    main()
