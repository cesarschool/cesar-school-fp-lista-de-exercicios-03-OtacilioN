## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234 @ 1, um F1 #, 2w3E *, 2We3345
# Então, a saída do programa deve ser:
# ABd1234 @ 1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

MAX_PASSWORD_LEN = 12
MIN_PASSWORD_LEN = 6
SPECIAL_CARACTERES = ['$', '#', '@']

def _validate_max_len(password):
    if(len(password) > MAX_PASSWORD_LEN):
        return False
    return True

def _validate_min_len(password):
    if(len(password) < MIN_PASSWORD_LEN):
        return False
    return True

def _validate_special_caracteres(password):
    for caracter in password:
        if(caracter in SPECIAL_CARACTERES):
            return True
    return False

def _validate_upper_caracteres(password):
    for caracter in password:
        if(caracter.isupper()):
            return True
    return False

def _validate_lower_caracteres(password):
    for caracter in password:
        if(caracter.islower()):
            return True
    return False

def _validate_numeric_caracteres(password):
    for caracter in password:
        if(caracter.isnumeric()):
            return True
    return False

def main():
    valid_passwords = [] 
    passwords = input().split(",")
    for password in passwords:
        if(_validate_max_len(password) and _validate_min_len(password) and _validate_special_caracteres(password) and _validate_upper_caracteres(password) and _validate_lower_caracteres(password) and _validate_numeric_caracteres(password)):
            valid_passwords.append(password)
    print(','.join(valid_passwords))
    


if __name__ == '__main__':
    main()
