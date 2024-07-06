import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path
import sqlite3

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agencia:\t{conta.agencia}
            Numero:\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        # TODO: validar o número de transações e invalidar a operação se for necessário
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("----- Você excedeu o número de transações permitidas para hoje! -----")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome 
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.id = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"

class Conta:
    def __init__(self, numero, cliente):        
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n ----- Operação falhou! Você não tem saldo. -----")

        elif valor > 0:
            self._saldo -= valor
            print("\n ----- Saque realizado com sucesso! -----")
             # Atualizar saldo no banco de dados
            cursor.execute("UPDATE contas SET saldo = ? WHERE numero = ?", (self._saldo, self._numero))
            conexao.commit()
            return True

        else:
            print("\n----- Operação falhou! O valor informado é inválido! -----")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n ----- Depósito realizado! -----")

            # Atualizar saldo no banco de dados
            cursor.execute("UPDATE contas SET saldo = ? WHERE numero = ?", (self._saldo, self._numero))
            conexao.commit()
            return True

        else:
            print("\n ----- Operação falhou! O valor informado é inválido! -----")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saldo = 0

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n ----- Operação falhou! O valor do saque excede o limite. -----")

        elif excedeu_saques:
            print("\n ----- Operação falhou! Número máximo de saques excedido. -----")

        else:
            return super().sacar(valor)
        
        return False
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"


    def __str__(self):
        return f"""\
            Agencia:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    # TODO: Filtrar todas as transações realizadas no dia
    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes
    
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def criar_tabelas(conexao, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        endereco TEXT NOT NULL
    )""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER NOT NULL,
        agencia TEXT NOT NULL,
        cliente_id INTEGER NOT NULL,
        saldo REAL NOT NULL,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )""")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, data_nascimento, cpf, endereco):
    cursor.execute("""
    INSERT INTO usuarios (nome, data_nascimento, cpf, endereco)
    VALUES (?, ?, ?, ?)
    """, (nome, data_nascimento, cpf, endereco))
    conexao.commit()
    return cursor.lastrowid

def inserir_conta(conexao, cursor, conta):

    cursor.execute("SELECT id FROM usuarios WHERE cpf = ?", (conta.cliente.cpf,))
    cliente_id = cursor.fetchone()[0]
    cursor.execute("""
    INSERT INTO contas (numero, agencia, cliente_id, saldo)
    VALUES (?, ?, ?, ?)
    """, (conta.numero, conta.agencia, conta.cliente.id, conta.saldo))
    conexao.commit()

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # TODO: alterar a implementação para salvar em arquivo
        
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n")
        
        return resultado
    
    return envelope

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.conta:
        print("\n ----- Cliente não possui conta! -----")
        return
    
    return cliente.conta[0]

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n ----- Cliente não encontrado! -----")
        return
    
     # Listar contas do cliente
    print("\n ----- Escolha a conta para depositar -----")
    for idx, conta in enumerate(cliente.conta, start=1):
        print(f"{idx}. Conta {conta.numero} - Saldo: R$ {conta.saldo:.2f}")

    try:
        escolha = int(input("Digite o número da conta: "))
        conta = cliente.conta[escolha - 1]
    except (ValueError, IndexError):
        print("\n ----- Opção inválida! -----")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n ----- Cliente não encontrado! ------")
        return
        
     # Listar contas do cliente
    print("\n ----- Escolha a conta para sacar -----")
    for idx, conta in enumerate(cliente.conta, start=1):
        print(f"{idx}. Conta {conta.numero} - Saldo: R$ {conta.saldo:.2f}")

    try:
        escolha = int(input("Digite o número da conta: "))
        conta = cliente.conta[escolha - 1]
    except (ValueError, IndexError):
        print("\n ----- Opção inválida! -----")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n ----- Cliente não encontrado! -----")
        return

    # Listar contas do cliente
    contas_cliente = cliente.conta
    if not contas_cliente:
        print("\n ----- Cliente não possui contas! -----")
        return

    print("\n --- Contas do Cliente --- ")
    for idx, conta in enumerate(contas_cliente, start=1):
        print(f"{idx}. Agência: {conta.agencia} | Conta: {conta.numero}")

    try:
        escolha = int(input("\nInforme o número da conta para exibir o extrato: "))
        conta_escolhida = contas_cliente[escolha - 1]

        print("\n ---------------- EXTRATO ---------------- ")

        extrato = ""
        tem_transacao = False
        for transacao in conta_escolhida.historico.gerar_relatorio():
            if transacao["valor"] != 0:
                tem_transacao = True
                extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
            elif tem_transacao:
                extrato = "Não foram realizadas movimentações."

        print(extrato)
        print(f"\nSaldo:\nR$ {conta_escolhida.saldo:.2f}")
        print("--------------------------------------------")

    except IndexError:
        print("\n ----- Conta selecionada inválida! -----")
    except ValueError:
        print("\n ----- Opção inválida! Informe um número de conta válido. -----")


@log_transacao
def criar_cliente(conexao, cursor, clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n ------ Já existe cliente com esse CPF! -----")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    try:
        # Insere o cliente no banco de dados e recupera o ID inserido
        id_cliente = inserir_registro(conexao, cursor, nome, data_nascimento, cpf, endereco)
        
        cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        setattr(cliente, 'id', id_cliente)  # Define o atributo id no objeto cliente
        
        clientes.append(cliente)

        print("\n ----- Cliente criado com sucesso! -----")

        return id_cliente  # Retorna o ID do cliente criado
    
    except sqlite3.IntegrityError as e:
        print(f"\n ------ Erro ao inserir cliente: {e} -----")

    print("\n ----- Cliente criado com sucesso! -----")

@log_transacao
def criar_conta(numero_conta, clientes, contas, conexao, cursor):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n ----- Cliente não encontrado, deseja criar um novo cliente? -----")
        return
    
        # Verifica se o cliente já possui um id no banco de dados
    if not hasattr(cliente, 'id'):
        # Cria o cliente no banco de dados
        cliente_id = criar_cliente(conexao, cursor, clientes)
        cliente.id = cliente_id  # Define o id no objeto cliente

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite = 500, limite_saques = 50)
    contas.append(conta)
    cliente.conta.append(conta)

    inserir_conta(conexao, cursor, conta)

    print("\n ------ Conta criada com sucesso! -----")

def listar_contas(contas):
    cursor.execute("""
    SELECT c.numero, c.agencia, u.nome as cliente_nome, c.saldo
    FROM contas c
    JOIN usuarios u ON c.cliente_id = u.id
    """)
    contas = cursor.fetchall()

    if not contas:
        print("\n ----- Não há contas cadastradas! -----")
        return
    
    print("=" * 100)
    for conta in contas:
        print(f"""\
            Agencia:\t{conta['agencia']}
            Numero:\t{conta['numero']}
            Titular:\t{conta['cliente_nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """)
    print("=" * 100)


def main():
    clientes = []
    contas = []
    # Carregar clientes e contas do banco de dados
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        cliente = PessoaFisica(nome=row['nome'], data_nascimento=row['data_nascimento'],
                               cpf=row['cpf'], endereco=row['endereco'])
        cliente.id = row['id']
        clientes.append(cliente)

    cursor.execute("SELECT * FROM contas")
    for row in cursor.fetchall():
        cliente = next((c for c in clientes if c.id == row['cliente_id']), None)
        if not cliente:
            print(f"Cliente não encontrado para a conta {row['numero']}")
            continue

        conta = ContaCorrente(numero=row['numero'], cliente=cliente)
        conta._saldo = row['saldo']  # Definir o saldo diretamente no atributo privado _saldo
        contas.append(conta)
        cliente.conta.append(conta)

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(conexao, cursor, clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas, conexao, cursor)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n ----- Operação inválida, por favor selecione novamente a operação desejada. -----")

criar_tabelas(conexao,cursor)
main()