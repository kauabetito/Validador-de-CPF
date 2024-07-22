# Validador de CPF 
from re import sub

while True:
    cpf_user = (input('\n\033[1;33;40mDigite um cpf sem os pontos e barras . - : '))
    cpf_user = sub(r'[^0-9]', '', cpf_user)  # removendo caracteres especiais para não dar erro no código
    cpf_standard = '00000000000'
    sequential_input = cpf_user == cpf_user[0] * len(cpf_user) # vereficando se o usuario digitou numeros repetidos

    if sequential_input:
        print('\n\033[1;31;40mVocê enviou números iguais')
        continue

    if len(cpf_user) == len(cpf_standard):
        break

    elif len(cpf_user) != len(cpf_standard):
        print('\n\033[1;31;40mVocê digitou o CPF errado um cpf tem 11 digitos!!!, digite novamente\033[m')



nine_digits = cpf_user[:9] # Fatiando o cpf até o numero 9
ten_digits = cpf_user[:10] # Fatiando o cpf até o numeor 10
countdown_1 = 10 # Contador Regressivo para a validação do primeiro digito
countdown_2 = 11 # Contador Regressivo para a validação do segundo digito
slicer_1 = 0 # Fatiador progressivo para a validação do primeiro digito
slicer_2 = 0 # Fatiador progressivo para a validação do segundo digito
first_digit_sum = 0
second_digit_sum = 0

while True: # Validação do primeiro digito
    digit = int(nine_digits[slicer_1])
    result_1 = countdown_1 * digit

    slicer_1 += 1
    countdown_1 -= 1

    first_digit_sum += result_1

    if countdown_1 == 1:
        break

while True: # Validação do segundo digito
    digit_2 = int(ten_digits[slicer_2])
    result_2 = countdown_2 * digit_2

    slicer_2 += 1
    countdown_2 -= 1

    second_digit_sum += result_2

    if countdown_2 == 1:
        break

first_digit = first_digit_sum * 10 % 11 # Conta final da validação do primeiro digito

second_digit = second_digit_sum * 10 % 11 # Conta final da validação do segundo digito

if first_digit > 9:
    first_digit = 0

if second_digit > 9:
    second_digit = 0

cpf_calculated = f'{nine_digits}{first_digit}{second_digit}'

if cpf_calculated == cpf_user:
    print(f'\n\033[1;32;40mo CPF que o usuario inseriu {cpf_user} é valido\033[m')
else:
    print(f'\n\033[1;31;40mCPF que o usuario inseriu {cpf_user} é invalido\033[m')
