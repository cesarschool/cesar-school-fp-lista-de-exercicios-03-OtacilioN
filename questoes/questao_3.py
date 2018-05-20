## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

CIMA = 1
DIREITA = 1
BAIXO = -1
ESQUERDA = -1
X_AXIS = 0
Y_AXIS = 1
AXIS_INDEX = 0
VALUE_INDEX = 1


def _move_robot(instruction, universe):
    # X_AXIS
    if(len(instruction) != 2):
        return universe
    if(instruction[AXIS_INDEX] == 'ESQUERDA'):
        universe[X_AXIS] = universe[X_AXIS] + int(instruction[VALUE_INDEX]) * ESQUERDA
    elif(instruction[AXIS_INDEX] == 'DIREITA'):
        universe[X_AXIS] = universe[X_AXIS] + int(instruction[VALUE_INDEX]) * DIREITA

    # Y_AXIS
    elif(instruction[AXIS_INDEX] == 'CIMA'):
        universe[Y_AXIS] = universe[Y_AXIS] + (int(instruction[VALUE_INDEX]) * CIMA)
    elif(instruction[AXIS_INDEX] == 'BAIXO'):
        universe[Y_AXIS] = universe[Y_AXIS] + int(instruction[VALUE_INDEX])  * BAIXO
    return universe

def _apply_pitagoras(universe):
    return (universe[X_AXIS]**2+universe[Y_AXIS]**2)**0.5

def main():
    universe = [0, 0]
    user_input = input().split()
    while(user_input):
        universe = _move_robot(user_input, universe)
        user_input = input().split()
    print(round(_apply_pitagoras(universe)))
    
if __name__ == '__main__':
    main()
