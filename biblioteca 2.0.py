import os
import time
import random

ID_usuario = random.randint(1000,9999)
ID_livro = random.randint(1000,9999)

# Função para gerar ID de usuário
def Gerar_iD_usuario(nome_usuario, ID_usuario):
    iniciais = nome_usuario[:2].upper()
    parte_numerica = f"{ID_usuario}"
    Novo_ID = iniciais + parte_numerica
    return Novo_ID

# Função para gerar ID de livro
def Gerar_iD_livro(tituloLivro):
    iniciais = tituloLivro[:2].upper()
    parte_numerica = f"{ID_livro}"
    Novo_ID_livro = iniciais + parte_numerica
    return Novo_ID_livro

#Função para criar o arquivo que guarda os livros
def criarBancoDeLivros(lista_de_Livros):
    with open ('lista_de_livros.txt','w') as arquivo:
        for livro in lista_de_Livros:
            arquivo.write(f'{livro.Titulo} | {livro.Autor} | {livro.CodigoLivro} | {livro.quantLivros}\n')
            
#classe para guarda as informações sobre cada livro
class Livro:
    def __init__(self, Titulo, Autor, CodigoLivro, quantLivros):
        self.Titulo = Titulo
        self.Autor = Autor
        self.CodigoLivro = CodigoLivro
        self.quantLivros =quantLivros
        
    def __str__(self):
        return f'Titulo: {self.Titulo}, Autor: {self.Autor},Codigo do livro: {self.CodigoLivro}, Quantidade de livros: {self.quantLivros}\n'

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
    cabecaBinlioteca()
    print("="*25,"Realizando cadastro","="*54)
        
    #colher informações
    nome_usuario = input('Digite o Nome do Usuário: ').upper()
    endereco_usuario = input("Digite o endereço do usuário: ").upper()
      
        #verificando se já existe usuario com mesmo nome
    with open('lista_de_usuarios.txt', 'r') as arquivo: 
                usuariosExistentes = arquivo.readlines()
                for linha in usuariosExistentes:
                    dados = linha.split('|')
                    nome_existente = dados[0].replace("Nome: ", "").strip()
                    if nome_usuario in nome_existente:
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
                print('='*100)
                print(f"Usuario:{nome_usuario}, cadastro com sucesso!")
                time.sleep(4.5)
                limparTela()
                escolherOpcao()            
    else:
        ('informações erradas, cadastro cancelado')  
        time.sleep(4.5)
        limparTela()
        escolherOpcao()
        
#Função para cadastrar os livros
def cadastroLivros():
    print("="*25,"Realizando cadastro","="*54)
    
    #colhendo informações
    Titulo = input("Qual o título do livro que deseja registrar? ").upper()
    Autor = input("Qual o autor do livro? ").upper()
    
    quant_livros = int(input("Qual a quantidade de exemplares disponíveis? "))
    
    # Verificando duplicidade no banco de livros
    try:
        with open('lista_de_livros.txt', 'r') as arquivo:
            livros_existentes = arquivo.readlines()
            for linha in livros_existentes:
                dados = linha.strip().split(" | ")  
                if Titulo == dados[0] and Autor == dados[1]:  # Comparando título e autor
                    print("=" * 100)
                    print(f'O livro "{Titulo}" do autor "{Autor}" já está cadastrado.')
                    time.sleep(4.5)
                    limparTela()
                    return cadastroLivros()  # Tenta novamente
    except FileNotFoundError:
        pass  # Se o arquivo não existe ainda, não há problema
   
    #Gerar o Codigo do livro
    Novo_ID_livro = Gerar_iD_livro(Titulo)
            
    #formatando o cadastro 
    print('='*100) 
    livroFormatado = (f'titulo: {Titulo} |Autor:{Autor} |ID de livro:{Novo_ID_livro}')
    print(livroFormatado)
            
    #confirmando operação
    print('='*100) 
    confirmacao = input("As informações mostradas estão corretas? (s/n): ").upper()
    if confirmacaoDeOperacao(confirmacao) == True: 
        with open('lista_de_livros.txt', 'a') as arquivo:           
                arquivo.write(livroFormatado + "\n")
                print('='*100)
                print(f"Livro:{Titulo}, cadastro com sucesso!")
                time.sleep(4.5)
                limparTela()
                
                
                
                escolherOpcao()            
    else:
        ('informações erradas, cadastro cancelado')  
        time.sleep(4.5)
        limparTela()
        escolherOpcao()
    
    #eviando informações para a classe Livro para que o objeto livro possa ser criado
    return Livro(Titulo, Autor, quant_livros)

#Função para criar o arquivo que guarda os usuarios
def criarBancoDeUsuarios(lista_de_usuarios):
    with open ('lista_de_usuarios.txt','w') as arquivo:
        for usuario in lista_de_usuarios:
            arquivo.write(usuario+"\n")    
            
#cabeçario da biblioteca 
def cabecaBinlioteca():
    print("="*25, "Bem-vindo ao acervo da Biblioteca", "="*40)
    
# Menu principal
def MenuInicial():
    cabecaBinlioteca()
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
    1: cadastroLivros,
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
            limparTela()
            if escolha in acoes:   
                acao = acoes[escolha] 
                acao()     
            else:
                print("="*100)
                print("Ação não permitida, tente novamente.")
                print("="*100)
                time.sleep(3.0)
                limparTela()
                escolherOpcao()        
        except ValueError: 
            print("="*100)
            print("Somente Números inteiros são aceitos!!")
            print("="*100)
            time.sleep(3.0)
            limparTela()
            escolherOpcao()
    
#função para limpar a tela 
def limparTela():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        clear_output()
escolherOpcao()