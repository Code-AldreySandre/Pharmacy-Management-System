def menu():
    # Exibe o menu de opções do sistema de gerenciamento de farmácia
    print("\nSistema de Gerenciamento de Farmácia")
    print("1. Cadastrar Medicamento")
    print("2. Cadastrar Funcionário")
    print("3. Buscar Medicamento")
    print("4. Buscar Funcionário")
    print("5. Imprimir Medicamentos")
    print("6. Imprimir Funcionários")
    print("7. Editar Medicamento")
    print("8. Editar Funcionário")
    print("9. Excluir Medicamento")
    print("10. Excluir Funcionário")
    print("11. Sair")

# Listas para armazenar os medicamentos e funcionários cadastrados como tuplas
medicamentos = []
funcionarios = []

def excluir_funcionario():
    # Solicita o nome do funcionário que será excluído
    nome = input("Digite o nome do funcionário que deseja excluir: ").lower()
    encontrado = False

    # Percorre a lista de funcionários e remove o funcionário encontrado
    for i, funcionario in enumerate(funcionarios):
        if funcionario[0].lower() == nome:
            funcionarios.pop(i)
            print(f"\nFuncionário '{funcionario[0]}' excluído com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"\nFuncionário '{nome}' não encontrado.")

def excluir_medicamento():
    # Solicita o nome do medicamento que será excluído
    nome = input("Digite o nome do medicamento que deseja excluir: ").lower()
    encontrado = False

    # Percorre a lista de medicamentos e remove o medicamento encontrado
    for i, medicamento in enumerate(medicamentos):
        if medicamento[0].lower() == nome:
            medicamentos.pop(i)
            print(f"\nMedicamento '{medicamento[0]}' excluído com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"\nMedicamento '{nome}' não encontrado.")

def editar_funcionario():
    # Solicita o nome do funcionário que será editado
    nome = input("Digite o nome do funcionário que deseja editar: ").lower()
    encontrado = False

    # Percorre a lista de funcionários e permite editar o funcionário encontrado
    for i, funcionario in enumerate(funcionarios):
        if funcionario[0].lower() == nome:
            print(f"\nFuncionário encontrado: Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Salário: {funcionario[2]}")
            print("Digite os novos dados (deixe em branco para manter o atual):")
            
            novo_nome = input("Novo nome: ")
            novo_cargo = input("Novo cargo: ")
            novo_salario = input("Novo salário: ")

            # Atualiza os dados do funcionário, mantendo os antigos se os novos forem deixados em branco
            nome_atualizado = novo_nome if novo_nome else funcionario[0]
            cargo_atualizado = novo_cargo if novo_cargo else funcionario[1]
            salario_atualizado = float(novo_salario) if novo_salario else funcionario[2]

            funcionarios[i] = (nome_atualizado, cargo_atualizado, salario_atualizado)
            print(f"\nFuncionário '{nome_atualizado}' atualizado com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"\nFuncionário '{nome}' não encontrado.")

def editar_medicamento():
    # Solicita o nome do medicamento que será editado
    nome = input("Digite o nome do medicamento que deseja editar: ").lower()
    encontrado = False

    # Percorre a lista de medicamentos e permite editar o medicamento encontrado
    for i, medicamento in enumerate(medicamentos):
        if medicamento[0].lower() == nome:
            print(f"\nMedicamento encontrado: Nome: {medicamento[0]}, Preço: {medicamento[1]}, Quantidade: {medicamento[2]}")
            print("Digite os novos dados (deixe em branco para manter o atual):")

            novo_nome = input("Novo nome: ")
            novo_preco = input("Novo preço: ")
            nova_quantidade = input("Nova quantidade: ")

            # Atualiza os dados do medicamento, mantendo os antigos se os novos forem deixados em branco
            nome_atualizado = novo_nome if novo_nome else medicamento[0]
            preco_atualizado = float(novo_preco) if novo_preco else medicamento[1]
            quantidade_atualizada = int(nova_quantidade) if nova_quantidade else medicamento[2]

            medicamentos[i] = (nome_atualizado, preco_atualizado, quantidade_atualizada)
            print(f"\nMedicamento '{nome_atualizado}' atualizado com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print(f"\nMedicamento '{nome}' não encontrado.")

def imprimir_funcionarios():
    # Verifica se há funcionários cadastrados
    if len(funcionarios) == 0:
        print("\nNão há funcionários cadastrados.")
        return

    # Solicita se o usuário deseja imprimir todos os funcionários ou um intervalo específico
    print("\nDeseja imprimir todos os funcionários ou um intervalo específico?")
    escolha = input("Digite 'tudo' para imprimir todos ou 'intervalo' para imprimir um intervalo: ")

    if escolha.lower() == 'tudo':
        # Imprime todos os funcionários cadastrados
        print("\nLista de Funcionários:")
        for funcionario in funcionarios:
            print(f"Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Salário: {funcionario[2]}")
    elif escolha.lower() == 'intervalo':
        # Permite ao usuário imprimir um intervalo de funcionários
        inicio = int(input("Digite o índice inicial: "))
        fim = int(input("Digite o índice final: "))

        if 0 <= inicio < len(funcionarios) and 0 <= fim <= len(funcionarios):
            print(f"\nFuncionários do índice {inicio} ao {fim}:")
            for i in range(inicio, fim):
                funcionario = funcionarios[i]
                print(f"Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Salário: {funcionario[2]}")
        else:
            print("Intervalo inválido.")
    else:
        print("Opção inválida.")

def imprimir_medicamentos():
    # Verifica se há medicamentos cadastrados
    if len(medicamentos) == 0:
        print("\nNão há medicamentos cadastrados.")
        return

    # Solicita se o usuário deseja imprimir todos os medicamentos ou um intervalo específico
    print("\nDeseja imprimir todos os medicamentos ou um intervalo específico?")
    escolha = input("Digite 'tudo' para imprimir todos ou 'intervalo' para imprimir um intervalo: ")

    if escolha.lower() == 'tudo':
        # Imprime todos os medicamentos cadastrados
        print("\nLista de Medicamentos:")
        for medicamento in medicamentos:
            print(f"Nome: {medicamento[0]}, Preço: {medicamento[1]}, Quantidade: {medicamento[2]}")
    elif escolha.lower() == 'intervalo':
        # Permite ao usuário imprimir um intervalo de medicamentos
        inicio = int(input("Digite o índice inicial: "))
        fim = int(input("Digite o índice final:"))

        if 0 <= inicio < len(medicamentos) and 0 <= fim <= len(medicamentos):
            print(f"\nMedicamentos do índice {inicio} ao {fim}:")
            for i in range(inicio, fim):
                medicamento = medicamentos[i]
                print(f"Nome: {medicamento[0]}, Preço: {medicamento[1]}, Quantidade: {medicamento[2]}")
        else:
            print("Intervalo inválido.")
    else:
        print("Opção inválida.")

def buscar_funcionario():
    # Solicita o nome do funcionário que será buscado
    nome = input("Digite o nome do funcionário que deseja buscar: ").lower()
    encontrado = False

    # Busca o funcionário na lista e exibe os dados se encontrado
    for funcionario in funcionarios:
        if funcionario[0].lower() == nome:
            print(f"\nFuncionário encontrado: Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Salário: {funcionario[2]}")
            encontrado = True
            break

    # Se o funcionário não for encontrado, exibe uma mensagem
    if not encontrado:
        print(f"\nFuncionário '{nome}' não encontrado.")

def buscar_medicamento():
    # Solicita o nome do medicamento que será buscado
    nome = input("Digite o nome do medicamento que deseja buscar: ").lower()
    encontrado = False

    # Busca o medicamento na lista e exibe os dados se encontrado
    for medicamento in medicamentos:
        if medicamento[0].lower() == nome:
            print(f"\nMedicamento encontrado: Nome: {medicamento[0]}, Preço: {medicamento[1]}, Quantidade: {medicamento[2]}")
            encontrado = True
            break

    # Se o medicamento não for encontrado, exibe uma mensagem
    if not encontrado:
        print(f"\nMedicamento '{nome}' não encontrado.")

def cadastrar_funcionario():
    # Solicita os dados do novo funcionário
    nome = input("Digite o nome do funcionário: ").lower()
    cargo = input("Digite o cargo do funcionário: ").lower()
    salario = float(input("Digite o salário do funcionário: "))

    # Cria uma tupla com os dados do funcionário e adiciona à lista de funcionários
    funcionario = (nome, cargo, salario)
    funcionarios.append(funcionario)
    print(f"\nFuncionário '{nome}' cadastrado com sucesso!")

def cadastrar_medicamento():
    # Solicita os dados do novo medicamento
    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    # Cria uma tupla com os dados do medicamento e adiciona à lista de medicamentos
    medicamento = (nome, preco, quantidade)
    medicamentos.append(medicamento)
    print(f"\nMedicamento '{nome}' cadastrado com sucesso!")

def sistema_gerenciamento():
    # Loop principal do sistema de gerenciamento
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_medicamento()
        elif opcao == '2':
            cadastrar_funcionario()
        elif opcao == '3':
            buscar_medicamento()
        elif opcao == '4':
            buscar_funcionario()
        elif opcao == '5':
            imprimir_medicamentos()
        elif opcao == '6':
            imprimir_funcionarios()
        elif opcao == '7':
            editar_medicamento()
        elif opcao == '8':
            editar_funcionario()
        elif opcao == '9':
            excluir_medicamento()
        elif opcao == '10':
            excluir_funcionario()
        elif opcao == '11':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o sistema de gerenciamento
sistema_gerenciamento()
