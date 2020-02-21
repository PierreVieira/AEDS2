class Pessoa():
    def __init__(self, nome: str):
        self._nome = nome
        self.telefones = []

    def adiciona_telefone(self, tel):
        self.telefones.append(tel)

    @property
    def nome(self):
        return self._nome

    # Métodos dunder
    def __str__(self):
        return f"{self._nome} - {self.telefones}"

    def __repr__(self):
        return self.__str__()


class Autor(Pessoa):
    def __init__(self, primeiro_nome: str, nome_do_meio: str, ultimo_nome: str = ''):
        nomes = (primeiro_nome, nome_do_meio, ultimo_nome)
        nome = ' '.join(nomes).strip()
        super().__init__(nome)
        self.nome_como_citado = self.nome[-1].upper() + self.nome[0].upper() + '.'


class Livro():
    def __init__(self, titulo: str, ano: int, autores: list):
        if titulo == '':
            raise ValueError('O título não pode ser vazio!')
        self.titulo = titulo
        self.ano = ano
        self.autores = autores
