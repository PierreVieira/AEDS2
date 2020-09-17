import time
from datetime import datetime

from heap import MaxHeap


class Cliente:
    def __init__(self, nome: str, idade: int, necessidades_especiais: bool):
        self.nome = nome
        self.idade = idade
        self.necessidades_especiais = necessidades_especiais

    def __str__(self):
        return self.nome

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade and self.necessidades_especiais == other.necessidades_especiais


class PrioridadeCliente:
    def __init__(self, cliente: Cliente, prioridade: int):
        self.cliente = cliente
        self.prioridade = prioridade
        self.horario_entrada = datetime.now()
        time.sleep(0.01)  # dorme um pouco para as comparações de prioridade serem satisfeitas

    def __eq__(self, outro: "PrioridadeCliente") -> bool:
        return False if self is None or outro is None else self.cliente == outro.cliente
        # É impossível um cliente ter a mesma prioridade que outro, pois é impossível eles
        # entrarem simultaneamente no banco, a não ser que seja o mesmo cliente.

    def __lt__(self, outro: "PrioridadeCliente") -> bool:
        return self.prioridade < outro.prioridade if self.prioridade != outro.prioridade else self.horario_entrada > outro.horario_entrada

    def __gt__(self, outro: "PrioridadeCliente") -> bool:
        return self.prioridade > outro.prioridade if self.prioridade != outro.prioridade else self.horario_entrada < outro.horario_entrada

    def __str__(self):
        return f"Cliente: {self.cliente} Prioridade: {self.prioridade}"

    def __repr__(self):
        return str(self)


class CaixaBanco:
    def __init__(self, nome_banco: str):
        self.fila_prioridade = MaxHeap()

        self.nome_banco = nome_banco

    def adiciona_cliente(self, cliente: Cliente):
        ordem_de_prioridade = 3 if cliente.idade >= 80 else (
            2 if cliente.idade >= 60 or cliente.necessidades_especiais else 1)
        nova_priodade = PrioridadeCliente(cliente, ordem_de_prioridade)
        self.fila_prioridade.insere(nova_priodade)

    def proximo_cliente(self) -> Cliente:
        return self.fila_prioridade.retira_max()

    @property
    def tem_cliente(self):
        return len(self) > 0

    def __str__(self):
        return f"Banco: {self.nome_banco} Fila: {self.fila_prioridade}"

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.fila_prioridade.arr_heap) - 1
