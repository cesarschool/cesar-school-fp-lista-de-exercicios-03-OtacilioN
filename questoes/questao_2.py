## QUESTÃO 2 ##
#
# Escreva um programa para calcular a frequencia das palavras de uma entrada. 
# A saída deve mostrar a frequencia depois de ordenar a chave alfanumericamente.
# Suponha que a seguinte entrada seja fornecida ao programa:
#     New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# Então, a saída deve ser:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def print_word_count(word, user_input):
    print(word+':'+str(user_input.count(word)))

def main():
    user_input = input().split()
    user_input.sort()
    print_word_count(user_input[0], user_input)
    for word in range(1, len(user_input)):
        if(user_input[word] != user_input[word-1]):
            print_word_count(user_input[word], user_input)
        
if __name__ == '__main__':
    main()
