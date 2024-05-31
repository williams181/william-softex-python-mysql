class Create:
    def __init__(self, conn):
        self.cursor = conn.cursor

    def execute_query(self, query: str, values=None):
        if values is None:
            values = []
        try:
            self.cursor.execute(query, values)
        except Exception as e:
            print("Error: Can't execute query", e)

    def create_db(self):
        query_create = """CREATE SCHEMA IF NOT EXISTS loja;"""
        self.execute_query(query_create)

    def use_db(self):
        query = """USE loja;"""
        self.execute_query(query)

    def drop_db(self):
        query = """DROP SCHEMA loja;"""
        self.execute_query(query)

    def create_table_cliente(self):
        query = """CREATE TABLE IF NOT EXISTS loja.cliente (
                        id_cliente INT NOT NULL PRIMARY KEY,
                        nome_cliente VARCHAR(50) NOT NULL,
                        endereco VARCHAR(30) NOT NULL,
                        cidade VARCHAR(30) NOT NULL,
                        cep VARCHAR(9) NOT NULL,
                        UF VARCHAR(2) NOT NULL
                    );"""
        self.execute_query(query)

    def create_table_vendedor(self):
        query = """CREATE TABLE IF NOT EXISTS loja.vendedor (
                                id_vendedor INT NOT NULL PRIMARY KEY,
                                nome_vendedor VARCHAR(50) NOT NULL,
                                salario_fixo INT NOT NULL,
                                faixa_comissao INT
                            );"""
        self.execute_query(query)

    def create_table_pedido(self):
        query = """CREATE TABLE IF NOT EXISTS loja.pedido (
                                        id_pedido INT NOT NULL PRIMARY KEY,
                                        prazo_entrega DATE NOT NULL,
                                        id_vendedor INT NOT NULL,
                                        id_cliente INT NOT NULL,
                                        FOREIGN KEY (id_vendedor) REFERENCES vendedor(id_vendedor),
                                        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
                                    );"""
        self.execute_query(query)

    def create_table_produto(self):
        query = """CREATE TABLE IF NOT EXISTS loja.produto (
                                                id_produto INT NOT NULL PRIMARY KEY,
                                                unidade INT NOT NULL,
                                                descricao VARCHAR(50),
                                                valor FLOAT NOT NULL
                                            );"""
        self.execute_query(query)

    def create_table_item_pedido(self):
        query = """CREATE TABLE IF NOT EXISTS loja.item_pedido (
                                                id_produto INT NOT NULL,
                                                id_pedido INT NOT NULL,
                                                quantidade INT NOT NULL,
                                                PRIMARY KEY (id_produto, id_pedido)
                                            );"""
        self.execute_query(query)

    def create_tables(self):
        self.create_table_cliente()
        self.create_table_vendedor()
        self.create_table_produto()
        self.create_table_pedido()
        self.create_table_item_pedido()

    def populate_cliente(self):
        query =  """INSERT INTO loja.cliente (
                        id_cliente,
                        nome_cliente,
                        endereco,
                        cidade,
                        cep,
                        UF)
                    VALUES
                    (1, 'jorge', 'rua um', 'Recife', '515151-05', 'PE'),
                    (2, 'luciana', 'rua dois', 'Olinda', '515151-06', 'PE'),
                    (3, 'lucas', 'rua tres', 'Recife', '515151-07', 'PE'),
                    (4, 'ana', 'rua um', 'Olinda', '515151-05', 'PE'),
                    (5, 'cecilia', 'rua dois', 'São Paulo', '516151-06', 'SP'),
                    (6, 'matheus', 'rua tres', 'Recife', '515151-07', 'PE');
                    """
        self.execute_query(query)

    def populate_vendedor(self):
        query =  """INSERT INTO loja.vendedor (
                        id_vendedor,
                        nome_vendedor,
                        salario_fixo,
                        faixa_comissao)
                    VALUES
                    (1, 'jeff', 3000, 200),
                    (2, 'felipe', 4000, 500);
                    """
        self.execute_query(query)

    def populate_produto(self):
        query =  """INSERT INTO loja.produto (
                        id_produto,
                        unidade,
                        descricao,
                        valor)
                    VALUES
                    (1, 400, 'caneta', 1.15), 
                    (2, 250, 'lapis', 1.00), 
                    (3, 100, 'caderno', 14.15), 
                    (4, 40, 'placa de video', 1756.98), 
                    (5, 60, 'processador', 540.99), 
                    (6, 70, 'caderneta', 105.15), 
                    (7, 120, 'teclado', 74.00), 
                    (8, 120, 'mouse', 13.99), 
                    (9, 30, 'headset', 1500.75), 
                    (10, 4, 'notebook', 15000);
                    """
        self.execute_query(query)


    def populate_pedido(self):
        query =  """INSERT INTO loja.pedido(
                        id_pedido,
                        prazo_entrega,
                        id_vendedor,
                        id_cliente)
                    VALUES
                    (1, STR_TO_DATE('05/06/2024', '%d/%m/%Y'), 1, 1),
                    (2, STR_TO_DATE('05/06/2024', '%d/%m/%Y'), 1, 1),
                    (3, STR_TO_DATE('14/07/2024', '%d/%m/%Y'), 2, 2),
                    (4, STR_TO_DATE('23/07/2024', '%d/%m/%Y'), 1, 3),
                    (5, STR_TO_DATE('27/07/2024', '%d/%m/%Y'), 2, 4),
                    (6, STR_TO_DATE('01/07/2024', '%d/%m/%Y'), 2, 4),
                    (7, STR_TO_DATE('09/08/2024', '%d/%m/%Y'), 1, 5),
                    (8, STR_TO_DATE('21/11/2024', '%d/%m/%Y'), 1, 6);
                    """
        self.execute_query(query)

    def populate_item_pedido(self):
        query = """INSERT INTO loja.item_pedido(
                        id_produto,
                        id_pedido,
                        quantidade)
                    VALUES
                    (10, 1, 1),
                    (9, 1, 1),
                    (8, 1, 1),
                    (7, 1, 1),
                    (5, 1, 1),
                    (6, 2, 2),
                    (6, 3, 1),
                    (1, 4, 10),
                    (1, 5, 15),
                    (2, 5, 15),
                    (3, 5, 15),
                    (4, 6, 1),
                    (10, 7, 10),
                    (4, 8, 5),
                    (5, 8, 5);
                    """
        self.execute_query(query)

    def populate_tables(self):
        self.populate_cliente()
        self.populate_vendedor()
        self.populate_produto()
        self.populate_pedido()
        self.populate_item_pedido()