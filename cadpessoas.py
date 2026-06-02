import os

usuarios = []
email = []
telefone = []

status = 1


while status == 1 :
    print("\n----------- MENU -----------")
    print("1 - Fazer Cadastro")
    print("2 - Listar Usuarios")
    print("3 - Sair do sistema")
    print("\n----------- MENU -----------")
    opcao = input("Escolha uma opção acima: ")

    if opcao == "1":
        print("FAZER CADASTRO!")
        nome = input("Digite o seu nome : ")
        usuarios.append(usuarios) 
        
        email = input("Digite seu email :")
        usuarios.append(email)
        
        senha = input("Digite sua telefone :")
        usuarios.append(telefone)

        print("cadastro concluido!")
        os.system("cls") 
        
    elif opcao == "2":
        print("\n-------- CADASTRO EM ANDAMENTO -----------")
        print("NOME :", nome, "\t EMAIL: ", email, "\t TELEFONE: ", telefone)
        print("--------------------------------------------")
    elif opcao == "3":
        escolha = 2
        print("CADASTRO FINALIZADO.")
        os.system("cls") 
