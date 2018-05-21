## QUESTÃO 5 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
#
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26.
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular.
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg
#          Saída: trl
#	Entrada: ROT0 c
#          Saída: c
#	Entrada: ROT26 Cool
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog.
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem
# deve ser impressa: 'Erro'.
# Entradas inválidas podem ser entradas que contém códigos de rotações
# inválidos ou mensagens contendo caracteres que não estão no alfabeto.
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem',
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

LETTERS_IN_ALPHABET = 26


def _rotate(char, rot):
    rotated_char = ord(char)+rot
    if(char.isupper()):
        if(rotated_char <= ord('Z')):
            print()
            return chr(rotated_char)
        else:
            return chr(ord('A')+((rotated_char - ord('A')) % LETTERS_IN_ALPHABET))

    else:
        if(rotated_char <= ord('z')):
            return chr(rotated_char)
        else:
            return chr(ord('a')+((rotated_char - ord('a')) % LETTERS_IN_ALPHABET))


def main():
    rotated_word = []
    rotated_phrase = []
    user_input = input().split()
    rot_number = user_input[0].split('T')

    if(len(rot_number) != 2 or rot_number[0] != 'RO'):
        print('Erro')
        return

    rot_number = int(rot_number[1])
    del user_input[0]
    for word in user_input:
        for char in word:
            if(char == '.'):
                rotated_word.append(char)
            else:
                if(not char.isalpha()):
                    print('Erro')
                    return
                rotated_word.append(_rotate(char, rot_number))
        rotated_phrase.append(''.join(rotated_word))
        rotated_word = []

    print(' '.join(rotated_phrase))


if __name__ == '__main__':
    main()
