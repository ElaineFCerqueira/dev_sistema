tamanho_max = 20 #Definir o tamanho da pilha para 20 posições
pilha = []*tamanho_max #Inicialização da pilha
topo = -1 #Indicador do topo da pilha, inicia vazio

def vazia():
    if topo == -1:
        return True
    else:
        return False


def empilhar(nome):
    global topo #Modifica a variável topo definida fora da função

    if topo<tamanho_max:
        topo +=1            #soma uma posição na viável auxiliar topo
        pilha[topo] = nome
        print(f"{nome} foi cadastrdo com sucesso")
    else:
        print("Erro ao cadastrar a lista")

def desempilhar():
    global topo
    if not vazia():
        pilha[topo] = nome
        pilha[topo]=""              #Removendo a variável do topo
        topo -= 1
        print("Foi removido")
    else:
        print("Erro: a pilha esta vazia")

#LISTAR OS ELEMENTOS: É IGUAL A IDEIA DE LISTAR O VETOR

def listar():
    if pilha == []:
        print("A lista está vazia: \n")
        for num in pilha:
            print(num)
   
def  limpar():
    if not vazia():
        print("Elementos na pilha (no topo da base): ")
        for i in range(topo,-1,1):
            print(pilha[i])
    else:
        print("A pilha está vazia ")

while True:
    print("\n Escolha uma opção")
    print("1 - Empilhar a lista")
    print("2 - Desempilhar a lista")
    print("3 - Listar os elementos da lista")
    print("4 - Limpar a lista")
    print("5 - Sair")

    opcao = int(input("Digite sua opção"))
   
    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        empilhar(nome)
   
    elif opcao == 2:
        desempilhar()
   
    elif opcao == 3:
        listar()
   
    elif opcao == 4:
        limpar()

    elif opcao == 5:    
        print("Saindo do programa. Até logo!")  
        break

    else:
        print("Opção inválida!")




        max_size = 20 
pilha = [""] * max_size  
topo = -1  # 


def vazia():
    if topo == -1:
        return True
    else:
        return False


def empilhar(nome):
    global topo  
    if topo < max_size - 1: 
        topo += 1
        pilha[topo] = nome
        print(f"{nome} foi empilhado com sucesso.")
    else:
        print("Erro: A pilha está cheia!")


def desempilhar():
    global topo 
    if not vazia():
        nome = pilha[topo]
        pilha[topo] = ""  
        topo -= 1
        print(f"{nome} foi desempilhado.")
        return nome
    else:
        print("Erro: A pilha está vazia!")
        return None


def limpar():
    global topo  
    while not vazia():
        desempilhar()
    print("Pilha foi completamente esvaziada.")


def listar():
    if not vazia():
        print("Elementos na pilha (do topo para a base):")
        for i in range(topo, -1, -1):
            print(pilha[i])
    else:
        print("A pilha está vazia.")


while True:
    print("\nEscolha uma opção:")
    print("1 - Empilhar um nome")
    print("2 - Desempilhar")
    print("3 - Listar os elementos da pilha")
    print("4 - Limpar a pilha")
    print("5 - Sair")
   
    opcao = input("Digite sua opção: \n")
    print('\n')

    if opcao == '1':
        nome = input("Digite o nome para empilhar: ")
        empilhar(nome)
    elif opcao == '2':
        desempilhar()
    elif opcao == '3':
        listar()
    elif opcao == '4':
        limpar()
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")