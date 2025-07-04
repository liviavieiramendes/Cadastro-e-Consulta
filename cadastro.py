print("Bem-vindo! Nome: Livia Vieira Mendes")

lista_funcionarios = []
id_global = 5759

# Função para cadastrar e armazenar os dados dos funcionários
def cadastrar_funcionario(id):
    print (f'\nId do funcionário: {id}')
    nome = input("Nome: ")
    setor = input("Setor: ")
    salario = input("Salário: ")
    funcionario = {
        "id": int(id),
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    lista_funcionarios.append(funcionario.copy()) # O copy serve para que as informações de cada funcionário seja salvos independentemente e não afetem os outros registros em caso de remoção

# Função que vai buscar as infos salvas na função de cadastro e apresentar de acordo com a opção selecionada
def consultar_funcionarios():
    while True:
        print("\n1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            for f in lista_funcionarios:
                for chave, valor in f.items():
                    print(f"{chave}: {valor}")
        elif opcao == "2":
            id_busca = int(input("Digite o id: "))
            for f in lista_funcionarios:
                if f["id"] == id_busca:
                    for chave, valor in f.items():
                        print(f"{chave}: {valor}")
        elif opcao == "3":
            setor_busca = input("Digite o setor: ")
            for f in lista_funcionarios:
                if f["setor"] == setor_busca:
                    for chave, valor in f.items():
                        print(f"{chave}: {valor}")
        elif opcao == "4":
            return
        else:
            print("Opção inválida")

# Função para remover as informações do funcionário
def remover_funcionario():
    while True:
        id_remover = int(input("\nDigite o id do funcionário: "))
        for f in lista_funcionarios:
            if f["id"] == id_remover:
                lista_funcionarios.remove(f)
                print("Funcionário removido com sucesso.")
                return
        print("Id inválido")

# Menu fora das funções
while True:
    print("\n1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")
