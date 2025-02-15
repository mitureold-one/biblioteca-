import time
import os
import random

ID_livro = random.randint(1000,9999)

#função para limpar a tela 
def limparTela():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        clear_output()
        
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
        
# Função para gerar ID de livro
def Gerar_iD_livro(titulo):
    iniciais = titulo[:2].upper()
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

#Função para cadastrar os livros
def cadastroLivros():
    print("="*25,"Realizando cadastro","="*54)
    
    #colhendo informações
    Titulo = input("Qual o título do livro que deseja registrar? ").upper
    autor = input("Qual o autor do livro? ").upper
    
    quant_livros = int(input("Qual a quantidade de exemplares disponíveis? "))
    
    # Verificando duplicidade no banco de livros
    try:
        with open('lista_de_livros.txt', 'r') as arquivo:
            livros_existentes = arquivo.readlines()
            for linha in livros_existentes:
                dados = linha.strip().split(" | ")  
                if Titulo == dados[0] and autor == dados[1]:  # Comparando título e autor
                    print("=" * 100)
                    print(f'O livro "{Titulo}" do autor "{autor}" já está cadastrado.')
                    time.sleep(4.5)
                    limparTela()
                    return cadastroLivros()  # Tenta novamente
    except FileNotFoundError:
        pass  # Se o arquivo não existe ainda, não há problema
   
    #Gerar o Codigo do livro
    Novo_ID_livro= Gerar_iD_livro(Titulo, ID_livro)
            
    #formatando o cadastro 
    print('='*100) 
    livroFormatado = (f'titulo: {Titulo} |Autor:{autor} |ID de livro:{Novo_ID_livro}')
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
    return Titulo, autor, quant_livros

cadastroLivros()
