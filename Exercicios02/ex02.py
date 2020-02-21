from random import randint


class Pessoa():
    """
    @author: Pierre Vieira
    """

    def __init__(self, nome: str):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    # Métodos dunder
    def __str__(self):
        return self._nome

    def __repr__(self):
        return self.__str__()


class Autor(Pessoa):
    """
    @author: Pierre Vieira
    """

    def __init__(self, primeiro_nome: str, nome_do_meio: str, ultimo_nome: str = ''):
        nomes = (primeiro_nome, nome_do_meio, ultimo_nome)  # Cada parte do nome é um diferente elemento da tupla
        nome = ' '.join(nomes).strip()  # Reune os nomes na string nome
        super().__init__(nome)  # Chama o método super
        self._nome_como_citado = ultimo_nome.upper() + ' ' + self.nome[0].upper() + '.'  # Formata o nome

    @property
    def nome_como_citado(self):
        return self.nome_como_citado

    # Métodos dunder
    def __str__(self):
        return self._nome_como_citado

    def __repr__(self):
        return self.__str__()


class Livro():
    def __init__(self, titulo: str, ano: int, autores=None):
        if autores is None:  # Se não foi passado os autores como argumento para a função
            autores = []  # Os autores são uma lista vazia
        if titulo is None:  # Se o título é None (string vazia também é considerada como None)
            raise ValueError('O título não pode ser vazio!')  # Lance uma exceção informando o motivo
        else:  # Senão...
            self._titulo = titulo
            self._ano = ano
            self._autores = autores

    @property
    def titulo(self):
        return self._titulo

    @property
    def ano(self):
        return self._ano

    @property
    def autores(self):
        return self._autores

    # Métodos Dunder
    def __str__(self):
        return f'{self.titulo} // {self.ano}'

    def __repr__(self):
        return self.__str__()


class Biblioteca():
    def __init__(self, livros: list):
        self._livros_por_autor = self._calcular_livros_por_autor(livros)

    def _calcular_livros_por_autor(self, livros: list):
        """
        @author: Pierre Vieira
        :param livros: lista de livros
        :return: dicionário cuja key é o nome de um autor e o value é a lista de livros que esse autor já escreveu.
        """
        nomes = list(set(nome for livro in livros for nome in livro.autores))  # Ṕara cada nome em um livro da lista
        # de livros, adicione esses nomes a uma lista eliminando os nomes repetidos
        dicionario = {}  # Dicionário que irá ter como key o nome do autor e value a lista de livros que ele já escreveu
        for nome in nomes:  # Para cada nome na lista de nomes
            lista_livros_autor = []  # Cria uma lista vazia que irá armazenar os livros de cada autor
            for livro in livros:  # Ṕara cada livro na lista de livros
                if nome in livro.autores:  # Se o nome está incluso na lista de autores do livro
                    lista_livros_autor.append(livro)  # Adicione esse livro na lista de livros
            dicionario.update({nome: lista_livros_autor})  # Adicione ao dicionário um campo em que a o nome do autor
            # é a key e os livros escritos por esse autor é value
        return dicionario  # Retorne o dicionário gerado

    @property
    def livros_por_autor(self):
        return self._livros_por_autor

    # Métodos Dunder
    def __str__(self):
        return str(self._livros_por_autor)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lista_nomes = ('Pierre Martins Vieira', 'Maria Luiza Neves', 'Maria Eduarda Gonçalves', 'Victor Meyer Mello',
                   'Alexandro Jesus Vieira', 'Ana Claudia Fonseca Martins')
    titulos_livros = (
        'A Revolução dos Bichos', 'Fahrenheit 451', 'Dom Casmurro', 'A Bela e a Fera', 'Democracia: o Deus que Falhou',
        'Cálculo - Volume 2', 'Equações Diferenciais Elementares e Problemas de Valores de Contorno',
        'Era dos Extremos')
    lista_autores = [Autor(nome.split()[0], nome.split()[1], nome.split()[2]) for nome in lista_nomes]
    livros_para_bibloteca = []
    for titulo_livro in titulos_livros:
        ano = randint(1900, 2020)
        autores = [lista_autores[i] for i in range(randint(1, len(lista_autores) - 1), len(lista_autores), randint(1, 3))]
        livros_para_bibloteca.append(Livro(titulo_livro, ano, autores))
    biblioteca = Biblioteca(livros_para_bibloteca)
    for key, value in biblioteca.livros_por_autor.items():
        print(key, value)
