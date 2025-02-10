
from datetime import datetime
import os
import time
import random

#dicionarios, contadores e listas usados no programa
livros = []
usuarios = []
ID_usario = random.randint(1000,9999)
codigo_livro = 1
historico_emprestimos = {}
pilha_operacoes = []

# Menu principal
def Menu_inicial():
    print("="*25, "Bem-vindo ao acervo da Biblioteca", "="*25)
    print("Essa versão é altamente instável e passível de bugs: alpha V0.01")
    print("O que você gostaria de fazer?")
    print("[1] - Cadastrar um livro")
    print("[2] - Cadastrar um usuário")
    print("[3] - Pesquisar por usuário")
    print("[4] - Consulta de livros")
    print("[5] - Empréstimos de livros")
    print("[6] - Devolução de livros")
    print("[7] - Desfazer última operação (emprestimo/devolução)")
    print("[8] - Encerrar aplicação")


    escolha = int(input("\nDigite somente o número da seleção: "))
    #sistema para limpar o terminal, é multiplataforma
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        clear_output()

    if escolha == 1:
        Cadastrar_livro()
    elif escolha == 2:
        Cadastrar_usuario()
    elif escolha == 3:
        pesquisar_usuario()
    elif escolha == 4:
        exibir_colecao()
    elif escolha == 5:
        Emprestar_livro()
    elif escolha == 6:
        Devolver_livro()
    elif escolha == 7:
        Desfazer_operacao()
    elif escolha == 8:
        encerramento()
    else:
        print("Ação não permitida, tente novamente.")
        Menu_inicial()

# Função para gerar ID de usuário
def Gerar_iD_usuario(nome_usuario, ID_usario):
    iniciais = nome_usuario[:2].upper()
    parte_numerica = f"{ID_usario}"
    Novo_ID = iniciais + parte_numerica
    return Novo_ID

# Função para cadastrar usuário
def Cadastrar_usuario():
    global ID_usario
    informa_corretas = "N"
    while informa_corretas == "N":
        print("#"*25,"Realizando cadastro","#"*25)
        nome_usuario = input("Digite o Nome do Usuário: ").upper()
        endereco_usuario = input("Digite o endereço do usuário: ").upper()
        Novo_ID = Gerar_iD_usuario(nome_usuario, ID_usario)

        print("="*25, "Informações Cadastrais", "="*25)
        print(f"Usuário: {nome_usuario}\nEndereço: {endereco_usuario}")
        print("="*85)
        informa_corretas = input("As informações mostradas estão corretas? (s/n): ").upper()

        if informa_corretas == "S":
            usuario = {
                "Nome": nome_usuario,
                "Endereço": endereco_usuario,
                "ID": Novo_ID,
                "Livros Emprestados": []
            }
            usuarios.append(usuario)
            historico_emprestimos[Novo_ID] = []
            ID_usario += 1
            print("#"*25, "Usuário Cadastrado com Sucesso", "#"*27)
            print(f"Usuário: {nome_usuario}\nID: {Novo_ID}")

            time.sleep(2.0)
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            else:
                clear_output()

        elif informa_corretas != "N":
            print("Ação não disponível.")
            Cadastrar_usuario()

# Função para cadastrar livro
def Cadastrar_livro():
    global codigo_livro
    informa_corretas = "N"
    while informa_corretas == "N":
        print("#"*25,"Realizando cadastro","#"*25)
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        try:
            exemplares = int(input("Digite o número de exemplares disponíveis: "))
        except ValueError:
            print("Por favor, insira um número válido para o número de exemplares.")
            return

        print("="*25, "Informações Cadastrais", "="*25)
        print(f"Título: {titulo}\nAutor: {autor}\nN° de Exemplares: {exemplares}\nID do Livro: {codigo_livro}")
        print("="*85)
        informa_corretas = input("As informações estão corretas? (s/n): ").upper()

        if informa_corretas == "S":
            livro = {
                "Código": codigo_livro,
                "Título": titulo,
                "Autor": autor,
                "Exemplares": exemplares,
                "Emprestado": 0
            }
            livros.append(livro)
            print("#"*25, "Livro Cadastrado com Sucesso", "#"*27)
            print(f"Livro: {titulo}\nID do Livro: {codigo_livro}")
            print("#"*80)
            codigo_livro += 1

            time.sleep(3.5)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            Menu_inicial()

        elif informa_corretas == "N":
            print("Por favor, tente novamente.")

#Função emprestar livro
def Emprestar_livro():
    print('=' * 25, "Empréstimo de Livros", '=' * 25)
    nome_pesquisa = input("Digite o nome do usuário: ").upper()

    for usuario in usuarios:
        if usuario["Nome"] == nome_pesquisa:
            if len(usuario["Livros Emprestados"]) < 3:
                try:
                    codigo_livro = int(input("Digite o código do livro: "))
                except ValueError:
                    print("Código inválido.")
                    return

                prazo_devolucao = input("Quando o livro deve ser devolvido? (dd/mm/aaaa): ")
                data_emprestimo = datetime.now().strftime("%d/%m/%Y")  # Data atual

                for livro in livros:
                    if livro["Código"] == codigo_livro:
                        if livro["Exemplares"] > livro["Emprestado"]:
                            usuario["Livros Emprestados"].append({
                                "Título": livro["Título"],
                                "Data Empréstimo": data_emprestimo,
                                "Data Devolução": prazo_devolucao
                            })
                            livro["Emprestado"] += 1
                            print(f"Livro '{livro['Título']}' emprestado a {nome_pesquisa}. Data de devolução: {prazo_devolucao}.")
                            pilha_operacoes.append({
                                 "tipo": "empréstimo",
                                 "usuario": nome_pesquisa,
                                 "livro": livro["Título"],
                                 "data": data_emprestimo,
                                 "devolucao": prazo_devolucao
                            })
                            time.sleep(3.5)
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")
                            Menu_inicial()
                        else:
                            print("Não há exemplares disponíveis para este livro.")
                            Menu_inicial()
                        return
                print("Livro não encontrado.")
                Menu_inicial()
            else:
                print("O usuário já possui 3 livros emprestados.")
                Menu_inicial()
            return
    print("Usuário não encontrado.")
    Menu_inicial()


# Função para devolver livro
def Devolver_livro(data_emprestimo):
    print('=' * 25, "Devolução de Livros", '=' * 25)
    nome_pesquisa = input("Digite o nome do usuário: ").upper()

    for usuario in usuarios:
        if usuario["Nome"] == nome_pesquisa:
            if "Livros Emprestados" in usuario and usuario["Livros Emprestados"]:
                print("Livros emprestados por este usuário:")
                for idx, livro in enumerate(usuario["Livros Emprestados"], start=1):
                    print(f"{idx}. {livro['Título']} - Prazo de Devolução: {livro['Data Devolução']}")

                try:
                    indice_livro = int(input("Digite o número do livro a ser devolvido: ")) - 1
                    livro_a_devolver = usuario["Livros Emprestados"].pop(indice_livro)

                    for livro in livros:
                        if livro["Título"] == livro_a_devolver["Título"]:
                            livro["Emprestado"] -= 1
                            print(f"Livro '{livro['Título']}' devolvido com sucesso!")
                            pilha_operacoes.append({
                                "tipo": "devolução",
                                "usuario": nome_pesquisa,
                                "livro": livro_a_devolver["Título"],
                                "data": data_emprestimo
                            })
                            time.sleep(3.5)
                            if os.name == "nt":
                                os.system("cls")
                            else:
                                os.system("clear")
                            Menu_inicial()
                except (ValueError, IndexError):
                    print("Opção inválida. Tente novamente.")
                    Menu_inicial()
            else:
                print("O usuário não possui livros emprestados.")
                Menu_inicial()
            return
    print("Usuário não encontrado.")
    Menu_inicial()

# Função para pesquisar um usuário e exibir o histórico de empréstimos
def pesquisar_usuario():
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return

    nome = input("Digite o nome do usuário que você quer encontrar: ").upper()
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario.get("Nome", "").upper() == nome:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print("#"*100)
        print(f"\nUsuário encontrado:")
        print(f"ID: {usuario_encontrado.get('ID', 'ID não encontrado')}")
        print(f"Nome: {usuario_encontrado.get('Nome', 'Nome não encontrado')}")
        print(f"Endereço: {usuario_encontrado.get('Endereço', 'Endereço não encontrado')}")
        time.sleep(3.5)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        pesquisar_usuario()

        # Exibir histórico de empréstimos
        if usuario_encontrado["Livros Emprestados"]:
            print("\nHistórico de Empréstimos:")
            for emprestimo in usuario_encontrado["Livros Emprestados"]:
                print(f"Título: {emprestimo.get('Título', 'Título não encontrado')}, "
                      f"Data de Empréstimo: {emprestimo.get('Data Empréstimo', 'Data não encontrada')}, "
                      f"Data de Devolução: {emprestimo.get('Data Devolução', 'Data não encontrada')}")
                print("#"*100)
                time.sleep(3.5)
                if os.name == "nt":
                   os.system("cls")
                else:
                   os.system("clear")
                pesquisar_usuario()
        else:
            print("#"*100)
            print("Nenhum histórico de empréstimos para este usuário.")
            print("#"*100)
            time.sleep(3.5)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            pesquisar_usuario()
    else:
        print("Usuário não encontrado.")
        time.sleep(3.5)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        pesquisar_usuario()

#Função de exibir
def exibir_colecao():
    print("Lista de livros na biblioteca:")
    for livro in livros:
        print("="*100)
        print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Código: {livro['Código']}, Disponíveis: {livro['Exemplares'] - livro['Emprestado']}")
        print("="*100)
    Menu_inicial()

#Função de encerramento
def encerramento():
    print("*"*200)
    print("Programa encerrado. Obrigado por utilizar a biblioteca.")
    print("*"*200)
    time.sleep(2)
    exit()

#desfazer
def Desfazer_operacao():
    if not pilha_operacoes:
        print("Não há operações para desfazer.")
        Menu_inicial()
        return

    ultima_operacao = pilha_operacoes.pop()

    if ultima_operacao["tipo"] == "empréstimo":
        # Reverte o empréstimo
        for usuario in usuarios:
            if usuario["Nome"] == ultima_operacao["usuario"]:
                for i, livro_emprestado in enumerate(usuario["Livros Emprestados"]):
                    if livro_emprestado["Título"] == ultima_operacao["livro"]:
                        usuario["Livros Emprestados"].pop(i)
                        break
                break
        # Encontra o livro e decrementa o número de empréstimos
        for livro in livros:
            if livro["Título"] == ultima_operacao["livro"]:
                livro["Emprestado"] -= 1
                print(f"Empréstimo do livro '{livro['Título']}' desfeito com sucesso.")
                break
    elif ultima_operacao["tipo"] == "devolução":
        # Reverte a devolução
        for usuario in usuarios:
            if usuario["Nome"] == ultima_operacao["usuario"]:
                usuario["Livros Emprestados"].append({
                    "Título": ultima_operacao["livro"],
                    "Data Empréstimo": ultima_operacao["data"],
                    "Data Devolução": ultima_operacao.get("devolucao", "Data não disponível")
                })
                break
        # Incrementa o número de empréstimos para o livro
        for livro in livros:
            if livro["Título"] == ultima_operacao["livro"]:
                livro["Emprestado"] += 1
                print(f"Devolução do livro '{livro['Título']}' desfeita com sucesso.")
                break

    time.sleep(2)
    Menu_inicial()

Menu_inicial()