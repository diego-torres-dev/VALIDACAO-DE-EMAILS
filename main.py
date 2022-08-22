# Solicita que o usuário informe seus dados
nome = input("Informe seu nome:\n")
email = input("Digite seu email:\n")

# Verifica se os campos foram preenchidos
if nome and email:
    posicao_a = email.find("@")
    dominio = email[posicao_a:]
    if posicao_a != -1 and "." in dominio:
        print(f"{nome}, seu cadastro foi realizado com sucesso.")
    else:
        print(f"Oops! {nome}, o e-mail que você digitou é inválido")
else:
    print("Por favor, preencha todos os campos.")