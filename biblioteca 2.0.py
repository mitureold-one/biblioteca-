import os
import time
import random

ID_usuario = random.randint(1000,9999)

# Função para gerar ID de usuário
def Gerar_iD_usuario(nome_usuario, ID_usuario):
    iniciais = nome_usuario[:2].upper()
    parte_numerica = f"{ID_usuario}"
    Novo_ID = iniciais + parte_numerica
    return Novo_ID

#Função para confirma as informações
def confirmacaoDeOperacao (confirmacao):
    while True:
        try:
            if confirmacao == "S":
                return True
            elif confirmacao == "N":
                return False
            else:
                print("Responda Somente com (s) ou (n):")
        except ValueError:
            print("="*100)
            print("Use somente letras para responder !!")
            print("="*100)

#Função para realizar os cadastros 
def cadastroUsuario():
    print("="*25,"Realizando cadastro","="*25)
        
    #colher informações
    nome_usuario = input('Digite o Nome do Usuário: ').upper()
    endereco_usuario = input("Digite o endereço do usuário: ").upper()
      
        #verificando se já existe usuario com mesmo nome
    with open('lista_de_usuarios.txt', 'r') as arquivo: 
                usuariosExistentes = arquivo.readlines()
                for linha in usuariosExistentes:
                    if nome_usuario in linha:
                        print('='*100)
                        print(f'O nome de usuário:"{nome_usuario}", já está em uso, por favor tente outra opção.')
                        time.sleep(4.5)
                        limparTela()
                        return cadastroUsuario()
                        
    #Gerar o id único do usuario
    Novo_ID = Gerar_iD_usuario(nome_usuario, ID_usuario)
            
    #formatando o cadastro 
    print('='*100) 
    usuarioFormatado = (f'Nome: {nome_usuario} |Endereço:{endereco_usuario} |ID de usuario:{Novo_ID}')
    print(usuarioFormatado)
            
    #confirmando operação
    print('='*100) 
    confirmacao = input("As informações mostradas estão corretas? (s/n): ").upper()
    if confirmacaoDeOperacao(confirmacao) == True: 
        with open('lista_de_usuarios.txt', 'a') as arquivo:           
                arquivo.write(usuarioFormatado + "\n")
                print(f"Usuario:{nome_usuario}, cadastro com sucesso!")
                time.sleep(4.5)
                limparTela()
                escolherOpcao()            
    else:
        ('informações erradas, cadastro cancelado')  
        time.sleep(4.5)
        limparTela()
        escolherOpcao()
        

#Função para criar o arquivo que guarda os usarios
def criarBancoDeUsuarios(lista_de_usuarios):
    with open ('lista_de_usuarios.txt','w') as arquivo:
        for usuario in lista_de_usuarios:
            arquivo.write(usuario+"\n")    
            
#cabeçario da biblioteca 
def cabecaBinlioteca():
    print("="*25, "Bem-vindo ao acervo da Biblioteca", "="*40)
    
# Menu principal
def MenuInicial():
    Menu = [
        '[1] - Cadastrar um livro',
        '[2] - Cadastrar um usuário',
        '[3] - Pesquisar por usuário especifico',
        '[4] - Consultar livros no sistema',
        '[5] - realzar emprestimo de livros',
        '[6] - Devolução de livro',
        '[7] - Desfazer última operação (emprestimo/devolução)',
        '[8] - Encerrar aplicação"'
    ]
    for item in Menu:
        print(item)

#Função para validar escolhas:
def escolherOpcao():
    MenuInicial()
    acoes = {
    1: 'none',
    2: cadastroUsuario,
    3: 'pesquisarUsuario',
    4: 'consultarLivros',
    5: 'ealizarEmprestimo',
    6: 'devolucaoLivro',
    7: 'desfazerOperacao',
    8: 'encerrarAplicacao'
    }
    while True:
        try:
            print("="*100)
            escolha = int(input("Digite somente o número da seleção: "))
            if escolha in acoes:   
                acao = acoes[escolha] 
                acao()      
            else:
                print("="*100)
                print("Ação não permitida, tente novamente.")
                print("="*100)
                time.sleep(3.0)
                limparTela()        
        except ValueError: 
            print("="*100)
            print("Somente Números inteiros são aceitos!!")
            print("="*100)
            time.sleep(3.0)
            limparTela()
    
#função para limpar a tela 
def limparTela():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        clear_output()
cadastroUsuario()