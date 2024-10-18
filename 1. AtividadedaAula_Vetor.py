quantidadeUsuarios = int(input('Quantos usuários você quer cadastrar? ')) # ler dado digitado ao usuario


nomes = [""] * quantidadeUsuarios
idades = [0] * quantidadeUsuarios
emails = [""] * quantidadeUsuarios
usuarios_cadastrado = 0
i=0

def exibir_menu():
    print('''\n Menu de Opções:
          1 - Cadastrar novo usuario
          2 - Listar todos os usuários
          3 - Buscar usuário pelo nome
          4 - Sair do sistema
          ''')
    return int(input("Digite a opção desejada: \n"))

def buscar_usuario(nome_procurado):
        for i in range(quantidadeUsuarios): #percorre todos os usuarios cadastrados dentro do vetor
            if nomes[i] == nome_procurado:
                (f"Usuário encontrado: Nome: {nomes[i]}, Idade: {idades[i]} ")
            else:
                print(f"Usuário não localizado")
        return
    

while True:
    opcao = exibir_menu()

    if (opcao==1):
        if usuarios_cadastrado<quantidadeUsuarios:
            nome = input("Digite o nome do usuario: ")
            idade = int(input("Digite a idade: "))
            email = input("Digite o email: ")

            nomes[usuarios_cadastrado] = nome
            idades[usuarios_cadastrado] = idade
            emails[usuarios_cadastrado] = email

            usuarios_cadastrado+=1

            print(f"Usuario: {nome}, {idade} , {email} foram cadastrados com sucesso")
    
    elif (opcao==2):
        if usuarios_cadastrado == 0:
            print("A lista está vazia")
        else:
            for i in range(usuarios_cadastrado):
                print(f"\n Nome: {nomes[i]}, Idade: {idades[i]}, Email: {emails[i]}")    
    
    elif (opcao==3):
        nome_procurado = input("Digite o nome a ser localizado: ")
        buscar_usuario(nome_procurado)
        

    elif (opcao==4):
        print("Saindo do sistema, até mais.")
        break
    
    else:
        print("Opção Invalida, tente novamente")
        print(opcao)

        
