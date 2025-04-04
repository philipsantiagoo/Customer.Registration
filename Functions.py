from bibliotecas import *
from Dicas import *

class Funções():
    def limpa_tela(self):
        # Função que limpa os dados que você estava escrevendo, mas não salvou
        self.código.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.cidade.delete(0, END)
        self.cep.delete(0, END)
        self.bairro.delete(0, END)
        self.endereco.delete(0, END)

    # Funções que tem realção ao banco de dados

    def conecta_banco_dados(self):
        self.conecta = sqlite3.connect('clientes.bd')
        self.cursor = self.conecta.cursor()
        print('Conectando ao Banco de Dados')

    def desconecta_banco_dados(self):
        self.conecta.close()
        print('Desconectando o Banco de Dados')

    def montaTabelas(self):
        self.conecta_banco_dados()

        # Criação da Tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)          
                );
        """)

        self.conecta.commit()
        print('Banco de Dados Criado')
        self.desconecta_banco_dados()

    def variáveis(self):
        # Função de variáveis para evitar repetir muito
        self.cod = self.código.get()
        self.name = self.nome.get()
        self.fone = self.telefone.get()
        self.city = self.cidade.get()

    def add_cliente(self):
        # Função que tem relação direta com o banco de dados, pois é com ela que novos cadastros são salvos no banco de dados criado nas funções anteriores.
        self.variáveis()

        if self.nome.get() == '':
            msg = 'Para o cadastro de um novo cliente é necessário que seja adicionado ao menos um nome.'
            messagebox.showinfo('ATENÇÃO!', msg)
        else:
            self.conecta_banco_dados()

            self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
                                VALUES (?, ?, ?)""", (self.name, self.fone, self.city))

            self.conecta.commit()
            self.desconecta_banco_dados()
            self.select_lista()
            self.limpa_tela()

    def select_lista(self):
        # Junto a função 'add_clientes', é com essa função que se tem a atualização da interface gráfica. Ou seja, essa função atualiza a interface gráfica com os novos cadastros
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conecta_banco_dados()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
                                    ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCLI.insert("", END, values=i)

        self.desconecta_banco_dados()

    def OnDubleClick(self, event):
        # Função resposável por possibilitar a volta, com dois cliques, dos dados salvos e exibidos na interface gráfica a sua aletração.
        self.limpa_tela()
        self.listaCLI.selection()

        for i in self.listaCLI.selection():
            coluna1, coluna2, coluna3, coluna4 = self.listaCLI.item(
                i, 'values')
            self.código.insert(END, coluna1)
            self.nome.insert(END, coluna2)
            self.telefone.insert(END, coluna3)
            self.cidade.insert(END, coluna4)

    def delete_cliente(self):
        # Junto a função 'OnDubleClick', essa função faz-se capaz de deletar da interface gráfica e do banco de dados os clicentes selecionados
        self.variáveis()
        self.conecta_banco_dados()
        self.cursor.execute(
            """ DELETE FROM clientes WHERE cod = ? """, (self.cod,))
        self.conecta.commit()
        self.desconecta_banco_dados()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        # Junto a função 'OnDubleClick', essa função faz-se capaz de alterar os dados dos clientes selecionados.
        self.variáveis()
        self.conecta_banco_dados()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                            WHERE cod = ? """, (self.name, self.fone, self.city, self.cod))
        self.conecta.commit()
        self.desconecta_banco_dados()
        self.select_lista()
        self.limpa_tela()

    def buscar_cliente(self):
        # Junto a função 'OnDubleClick', essa função faz-se capaz de buscar algum cliente específico digitando ao menos uma letra na label 'Nome' ou 'Código'.
        self.conecta_banco_dados()
        self.listaCLI.delete(*self.listaCLI.get_children())

        nome = self.nome.get() + '%'
        codigo = self.código.get()

        if codigo:
            self.cursor.execute(
                """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
                WHERE cod = ? ORDER BY nome_cliente ASC """, (codigo,))
        else:
            self.cursor.execute(
                """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
                WHERE nome_cliente LIKE ? ORDER BY nome_cliente ASC """, (nome,))

        resultados = self.cursor.fetchall()
        # buscanomeCLI = self.cursor.fetchall()

        for i in resultados:
            self.listaCLI.insert("", END, values=i)

        self.limpa_tela()
        self.desconecta_banco_dados()

    def adiciona_baloes(self):
        # Junto as funções tooltip, essa função determina o que vai aparecer nos balões de ajuda.
        ToolTip(self.button_limpar, "Limpa todos os campos do formulário.")
        ToolTip(self.button_buscar, "Busca um cliente pelo nome.")
        ToolTip(self.button_novo, "Adiciona um novo cliente ao banco de dados.")
        ToolTip(self.button_alterar, "Clique duas vezes nos dados do cliente selecionado, modifique o que deseja e clique em alterar.")
        ToolTip(self.button_apagar, "Clique duas vezes nos dados do cliente selecionado para apagar.")
        ToolTip(self.button_cep, "Clique para buscar o CEP. \n Observe que o CEP vai fornecer a cidade, bairro e endereço, mas os demais dados devem ser preenchidos manualmente. \n Os dados fornecidos pelo CEP não são salvos no banco de dados. São apenas para captar informações.")
