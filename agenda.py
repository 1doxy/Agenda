# Agenda de Contatos

contatos = []  # Lista para armazenar os contatos

# Função para adicionar um contato
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("Marcar como favorito? (s/n): ").lower() == 's'
    
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': favorito
    }
    
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

# Função para visualizar todos os contatos
def visualizar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    
    for idx, contato in enumerate(contatos, start=1):
        favorito = " (Favorito)" if contato['favorito'] else ""
        print(f"{idx}. {contato['nome']} - {contato['telefone']} - {contato['email']}{favorito}")

# Função para editar um contato
def editar_contato():
    visualizar_contatos()
    if not contatos:
        return
    
    index = int(input("Digite o número do contato que deseja editar: ")) - 1
    if index < 0 or index >= len(contatos):
        print("Contato inválido.")
        return
    
    print("Deixe o campo vazio para manter o valor atual.")
    nome = input(f"Nome atual ({contatos[index]['nome']}): ") or contatos[index]['nome']
    telefone = input(f"Telefone atual ({contatos[index]['telefone']}): ") or contatos[index]['telefone']
    email = input(f"Email atual ({contatos[index]['email']}): ") or contatos[index]['email']
    favorito = input("Marcar como favorito? (s/n): ").lower()
    
    contatos[index]['nome'] = nome
    contatos[index]['telefone'] = telefone
    contatos[index]['email'] = email
    if favorito:
        contatos[index]['favorito'] = favorito == 's'
    
    print("Contato atualizado com sucesso!")

# Função para marcar/desmarcar contato como favorito
def marcar_favorito():
    visualizar_contatos()
    if not contatos:
        return
    
    index = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    if index < 0 or index >= len(contatos):
        print("Contato inválido.")
        return
    
    contatos[index]['favorito'] = not contatos[index]['favorito']
    status = "favorito" if contatos[index]['favorito'] else "não favorito"
    print(f"Contato {contatos[index]['nome']} agora é {status}.")

# Função para visualizar contatos favoritos
def visualizar_favoritos():
    favoritos = [contato for contato in contatos if contato['favorito']]
    if not favoritos:
        print("Nenhum contato marcado como favorito.")
        return
    
    for idx, contato in enumerate(favoritos, start=1):
        print(f"{idx}. {contato['nome']} - {contato['telefone']} - {contato['email']} (Favorito)")

# Função para apagar um contato
def apagar_contato():
    visualizar_contatos()
    if not contatos:
        return
    
    index = int(input("Digite o número do contato que deseja apagar: ")) - 1
    if index < 0 or index >= len(contatos):
        print("Contato inválido.")
        return
    
    contatos.pop(index)
    print("Contato apagado com sucesso!")

# Menu principal
def menu():
    while True:
        print("\n----- Agenda de Contatos -----")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar favorito")
        print("5. Ver favoritos")
        print("6. Apagar contato")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            visualizar_contatos()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            marcar_favorito()
        elif escolha == '5':
            visualizar_favoritos()
        elif escolha == '6':
            apagar_contato()
        elif escolha == '7':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar a aplicação
if __name__ == "__main__":
    menu()
