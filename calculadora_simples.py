menu = '''
-- MENU --

[1] Soma
[2] Multiplicação
[3] Divisão
[4] Subtração
[5] Sair
'''

def soma():
    print("Operação selecionada com sucesso!\n")
    numero1_soma = input("Informe o primeiro número: ")
    numero2_soma = input("Informe o segundo número:")
        
    try:
        numero1_soma_validado = float(numero1_soma)
        numero2_soma_validado = float(numero2_soma)
        resultado = numero1_soma_validado + numero2_soma_validado
        print("\nO resultado da soma é:", resultado)
        input("Pressione enter para voltar ao menu principal.")
    except ValueError:
            print("\nPor favor, informe números validos. (Para informar números decimais, utilize ., ex: 1.2")

def multiplicacao():
    print("Operação selecionada com sucesso!")
    
    print("Operação selecionada com sucesso!\n")
    numero1_mult = input("Informe o primeiro número: ")
    numero2_mult = input("Informe o segundo número:")
        
    try:
        numero1_mult_validado = float(numero1_mult)
        numero2_mult_validado = float(numero2_mult)
        resultado = numero1_mult_validado * numero2_mult_validado
        print("\nO resultado da multiplicação é:", resultado)
        input("Pressione enter para voltar ao menu principal.")
    except ValueError:
            print("\nPor favor, informe números validos. (Para informar números decimais, utilize ., ex: 1.2")

def divisao():
    print("Operação selecionada com sucesso!")
    
    print("Operação selecionada com sucesso!\n")
    numero1_div = input("Informe o primeiro número: ")
    numero2_div = input("Informe o segundo número:")
        
    try:
        numero1_div_validado = float(numero1_div)
        numero2_div_validado = float(numero2_div)
        resultado = numero1_div_validado / numero2_div_validado
        print("\nO resultado da divisão é:", resultado)
        input("Pressione enter para voltar ao menu principal.")
    except ValueError:
            print("\nPor favor, informe números validos. (Para informar números decimais, utilize ., ex: 1.2")
    except ZeroDivisionError:
        print("Não é possivel dividir por zero. Tente novamente.")

def subtracao():
    print("Operação selecionada com sucesso!\n")
    numero1_sub = input("Informe o primeiro número: ")
    numero2_sub = input("Informe o segundo número:")
        
    try:
        numero1_sub_validado = float(numero1_sub)
        numero2_sub_validado = float(numero2_sub)
        resultado = numero1_sub_validado - numero2_sub_validado
        print("\nO resultado da subtração é:", resultado)
        input("Pressione enter para voltar ao menu principal.")
    except ValueError:
            print("\nPor favor, informe números validos. (Para informar números decimais, utilize ., ex: 1.2")

while True:
    print(menu)
    Select_option = input("Selecione uma operação com base no seu número(ex: 1,2..):")
    
    if Select_option == '1':
        soma()
    elif Select_option == '2':
        multiplicacao()
    elif Select_option == '3':
        divisao()
    elif Select_option == '4':
        subtracao()
    elif Select_option == '5':
        print("O programa foi encerrado. Até mais!")
        break
    else:
        print("Opção invalida. Tente novamente.")