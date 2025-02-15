#Função para criar o arquivo que guarda os livros
def criarBancoDeLivros(lista_de_Livros):
    with open ('lista_de_livros.txt','w') as arquivo:
        for Livro in lista_de_Livros:
            arquivo.write(Livro+"\n")  