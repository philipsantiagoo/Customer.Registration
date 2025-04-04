from bibliotecas import *
from Validators import Validadores
from Reports import Relatórios
from Dicas import ToolTip
from Functions import Funções
from PlaceHolder import EntPlaceHold
import brazilcep


# Configurando e criando a janela
janela = Tk()


# FrontEND
class Application(Funções, Relatórios, Validadores):
    def __init__(self):
        # Atribuindo a janela criada a variável janela
        self.janela = janela
        self.validaEntradas()                          # ...
        self.tela()                                    # Chama a função tela( )
        self.frames_da_tela()                          # Chama a função frames_da_tela( )
        self.widgets_frame_1()                         # Chama a função widgets_frame_1( )
        self.lista_frame_2()                           # Chama a função lista_frame_2( )
        self.montaTabelas()                            # ...
        self.select_lista()                            # ...
        self.Menus()                                   # ...
        self.adiciona_baloes()
        janela.mainloop()                              # .mainlopp( ) Mostrando na tela

    def cepCorreios(self):
        try:
            # Obtém o CEP digitado
            zipcode = self.cep.get()

            # Busca o endereço pelo CEP
            dadosCEP = brazilcep.get_address_from_cep(zipcode)

            # Preenche os campos com os dados retornados
            self.cidade.delete(0, END)
            self.bairro.delete(0, END)
            self.endereco.delete(0, END)

            self.cidade.insert(0, dadosCEP.get('city', ''))
            self.bairro.insert(0, dadosCEP.get('district', ''))
            self.endereco.insert(0, f"{dadosCEP.get('street', '')}. {dadosCEP.get('uf', '')}")

            print(f"Dados do CEP: {dadosCEP}")

        except brazilcep.exceptions.CEPNotFound:
            messagebox.showerror("Erro", "CEP não encontrado.")
        except brazilcep.exceptions.InvalidCEP:
            messagebox.showerror("Erro", "CEP inválido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar o CEP: {e}")

    def tela(self):
        # Cria a tela base do programa
        # .title( ) Título da janela
        self.janela.title('Cadastro de Clientes')
        # .configure( ) Cor de fundo da janela
        self.janela.configure(background='#272e29')
        # .geometry( ) Tamanho da janela
        self.janela.geometry("700x500")
        # .resizable( ) Janela pode ser redimensionada
        self.janela.resizable(True, True)
        # .maxsize( ) Tamanho máximo da janela
        self.janela.maxsize(900, 700)
        # .minsize( ) Tamanho mínimo da janela
        self.janela.minsize(650, 400)

    def frames_da_tela(self):
        # Aqui é a função que determina o 'retângulo cinza' da parte de cima e da parte debaixo
        # Frames são áreas/caixas dentro da janela que separam os componentes
        # Cria o frame 1 e o frame 2, define a cor e a borda deles
        # .place( ) Posiciona com relx e rely de forma relativa o frame

        self.frame_1 = Frame(self.janela, bd=4, bg='#BEBEBE',
                             highlightbackground='#444d46', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.janela, bd=4, bg='#BEBEBE',
                             highlightbackground='#444d46', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        # Criando as abas e todos os botões de ambas as abas
        # Criando os botões e definindo o tamanho e a posição deles.
        # .place( ) Posiciona com relx e rely de forma relativa o botão
        # bd = 2 define a borda do botão
        # bg = '#708777' define a cor de fundo do botão
        # fg = 'white' define a cor da fonte do botão
        # font=('Verdana', 8, 'bold') define a fonte do botão

        # Abas
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background='#BEBEBE')
        self.aba2.configure(background='#BEBEBE')

        self.abas.add(self.aba1, text='Aba I')
        self.abas.add(self.aba2, text='Aba II')

        self.abas.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.98)

        # Botões
        self.button_limpar = Button(self.aba1, text='Limpar', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.limpa_tela)
        self.button_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.button_buscar = Button(self.aba1, text='Buscar', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.buscar_cliente)
        self.button_buscar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        self.button_novo = Button(self.aba1, text='Novo', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.add_cliente)
        self.button_novo.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)


        # Associa o evento de pressionar Enter ao método add_cliente
        self.janela.bind('<Return>', lambda event: self.add_cliente())
        # Associa o evento de pressionar Backspace ao método delete_cliente
        self.janela.bind('<BackSpace>', lambda event: self.delete_cliente())


        self.button_alterar = Button(self.aba1, text='Alterar', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.altera_cliente)
        self.button_alterar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.15)

        self.button_apagar = Button(self.aba1, text='Apagar', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.delete_cliente)
        self.button_apagar.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.15)


    # Criando a Label e a Entrada de 'Código'
        self.lb_código = Label(self.aba1, text='Código', bg='#BEBEBE')
        self.lb_código.place(relx=0.052, rely=0.05)

        self.código = Entry(self.aba1, validate="key", validatecommand=self.validate2)
        self.código.place(relx=0.051, rely=0.15, relwidth=0.07)     # cor bg='#e6e1e1'

    # Criando a Label e a Entrada de 'Nome'
        self.lb_nome = Label(self.aba1, text='Nome', bg='#BEBEBE')
        self.lb_nome.place(relx=0.051, rely=0.28)

        self.nome = EntPlaceHold(self.aba1, 'Digite o nome do cliente')
        self.nome.place(relx=0.05, rely=0.38, relwidth=0.398)



    # Criando a Entrada de 'CEP' e o Botão de 'CEP'
        self.button_cep = Button(self.aba1, text='CEP', bd=2, bg='#708777', fg='white', font=('Verdana', 8, 'bold'), command=self.cepCorreios)
        self.button_cep.place(relx=0.525, rely=0.35, relwidth=0.1, relheight=0.15)

        self.cep = EntPlaceHold(self.aba1, 'Digite o CEP do cliente')
        self.cep.place(relx=0.63, rely=0.38, relwidth=0.32)
    

    # Criando a Label e a Entrada de 'Bairro'
        self.lb_bairro = Label(self.aba1, text='Bairro', bg='#BEBEBE')
        self.lb_bairro.place(relx=0.525, rely=0.5)

        self.bairro = Entry(self.aba1, bg='white')
        self.bairro.place(relx=0.525, rely=0.6, relwidth=0.425)
    
    # Criando a Label e a Entrada de 'Endereço'
        self.lb_endereco = Label(self.aba1, text='Endereço', bg='#BEBEBE')
        self.lb_endereco.place(relx=0.525, rely=0.7)

        self.endereco = Entry(self.aba1, bg='white')
        self.endereco.place(relx=0.525, rely=0.8, relwidth=0.425)



    # Criando a Label e a Entrada de 'Telefone'
        self.lb_telefone = Label(self.aba1, text='Telefone', bg='#BEBEBE')
        self.lb_telefone.place(relx=0.051, rely=0.5)

        self.telefone = EntPlaceHold(self.aba1, 'Digite o telefone do cliente')
        self.telefone.place(relx=0.052, rely=0.6, relwidth=0.396)

    # Criando a Label e a Entrada de 'Cidade'
        self.lb_cidade = Label(self.aba1, text='Cidade', bg='#BEBEBE')
        self.lb_cidade.place(relx=0.051, rely=0.7)

        self.cidade = EntPlaceHold(self.aba1, 'Digite a cidade do cliente')
        self.cidade.place(relx=0.051, rely=0.8, relwidth=0.398)


    # Criando Botão na Aba II - Estado Civil
        self.Tipvar = StringVar()
        self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)", "Separado(a)")
        self.Tipvar.set("Estado Civil")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.015, rely=0.05, relwidth=0.2, relheight=0.2)
        self.popupMenu.configure(highlightthickness=0)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)

    # Criando Botão na Aba II - Ocupação
        self.Tipvar = StringVar()
        self.TipV = ("Agricultura", "Comércio", "Construção Civil", "Educação", "Saúde", "Serviços Gerais", "Transporte", "Administração", "Indústria", "Estudante", "Aposentado", "Desempregado")
        self.Tipvar.set("Ocupação")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.015, rely=0.28, relwidth=0.2, relheight=0.2)
        self.popupMenu.configure(highlightthickness=0)
        self.trabalho = self.Tipvar.get()
        print(self.trabalho)

    # Criando Botão na Aba II - Grau de Escolaridade
        self.Tipvar = StringVar()
        self.TipV = ("Analfabeto(a)", "Fund. Incompleto", "Fund. Completo", "Médio Incompleto", "Médio Completo", "Sup. Incompleto", "Sup. Completo", "Pós-graduação")
        self.Tipvar.set("Escolaridade")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.015, rely=0.51, relwidth=0.2, relheight=0.2)
        self.popupMenu.configure(highlightthickness=0)
        self.escolaridade = self.Tipvar.get()
        print(self.escolaridade)

    # Criando Botão na Aba II - Grau de Escolaridade
        self.Tipvar = StringVar()
        self.TipV = ("Masculino", "Feminino", "Não Binário", "Prefiro não dizer")
        self.Tipvar.set("Gênero")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.015, rely=0.74, relwidth=0.2, relheight=0.2)
        self.popupMenu.configure(highlightthickness=0)
        self.sexualidade = self.Tipvar.get()
        print(self.sexualidade)


    # Criando um calendário na Aba II
        self.calendario = Calendar(
            self.aba2,
            selectmode='day',
            year=2025,
            month=4,
            day=3,
            background='#708777',
            foreground='white',
            borderwidth=2
        )
        self.calendario.place(relx=0.258, rely=0.05, relwidth=0.5, relheight=0.89)

       # Dicionário para armazenar as anotações
        self.anotacoes = {}

        # Campo de texto para anotações
        self.text_anotacao = Text(self.aba2, wrap=WORD, font=("Arial", 7))
        self.text_anotacao.place(relx=0.8, rely=0.05, relwidth=0.18, relheight=0.7)

        # Botão para salvar a anotação
        self.button_salvar_anotacao = Button(
            self.aba2,
            text="Salvar Anotação",
            bg="#708777",
            fg="white",
            font=("Arial", 7, "bold"),
            command=self.salvar_anotacao
        )
        self.button_salvar_anotacao.place(
            relx=0.8, rely=0.77, relwidth=0.18, relheight=0.08)

        # Botão para carregar a anotação
        self.button_carregar_anotacao = Button(
            self.aba2,
            text="Carregar Anotação",
            bg="#708777",
            fg="white",
            font=("Arial", 7, "bold"),
            command=self.carregar_anotacao
        )
        self.button_carregar_anotacao.place(
            relx=0.8, rely=0.859, relwidth=0.18, relheight=0.08)

    def salvar_anotacao(self):
        data = self.calendario.get_date()
        anotacao = self.text_anotacao.get("1.0", END).strip()
        if anotacao:
            self.anotacoes[data] = anotacao
            messagebox.showinfo("Sucesso", f"Anotação para {data} salva com sucesso!")
        else:
            messagebox.showwarning("Aviso", "O campo de anotação está vazio.")

    def carregar_anotacao(self):
        data = self.calendario.get_date()
        anotacao = self.anotacoes.get(data, "")
        self.text_anotacao.delete("1.0", END)
        self.text_anotacao.insert("1.0", anotacao)
        if anotacao:
            messagebox.showinfo("Sucesso", f"Anotação para {data} carregada com sucesso!")
        else:
            messagebox.showinfo("Aviso", f"Não há anotações para {data}.")

    def lista_frame_2(self):
        # Função responsável pelas atribuições do 'rentângulo cinza' da parte debaixo, sua interface gráfica.
        # Criando as abas no frame_2
        self.abas_frame2 = ttk.Notebook(self.frame_2)
        self.aba1_frame2 = Frame(self.abas_frame2)
        self.aba2_frame2 = Frame(self.abas_frame2)

        self.aba1_frame2.configure(background='#BEBEBE')
        self.aba2_frame2.configure(background='#BEBEBE')

        self.abas_frame2.add(self.aba1_frame2, text='Aba I')
        self.abas_frame2.add(self.aba2_frame2, text='Aba II')

        self.abas_frame2.place(relx=0.01, rely=0.01,
                               relwidth=0.98, relheight=0.98)

        # Aba I - Lista de Clientes
        self.listaCLI = ttk.Treeview(self.aba1_frame2, height=3, columns=(
            'coluna1', 'coluna2', 'coluna3', 'coluna4'))
        self.listaCLI.heading('#0', text='')
        self.listaCLI.heading('#1', text='Código')
        self.listaCLI.heading('#2', text='Nome')
        self.listaCLI.heading('#3', text='Telefone')
        self.listaCLI.heading('#4', text='Cidade')

        self.listaCLI.column('#0', width=1, stretch=NO)
        self.listaCLI.column('#1', width=50, anchor=CENTER)
        self.listaCLI.column('#2', width=200, anchor=W)
        self.listaCLI.column('#3', width=125, anchor=W)
        self.listaCLI.column('#4', width=125, anchor=W)

        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Treeview", background="#A9A9A9",
                         foreground="black", rowheight=25, fieldbackground="#A9A9A9")
        estilo.configure("Treeview.Heading", background="#708777",
                         foreground="white", font=('Verdana', 10, 'bold'))

        self.listaCLI.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroll_frame = Frame(self.aba1_frame2, bg="#BEBEBE")
        self.scroll_frame.place(relx=0.96, rely=0.1,
                                relwidth=0.03, relheight=0.85)

        self.scrool_lista = Scrollbar(
            self.scroll_frame, orient='vertical', relief=FLAT, borderwidth=0)
        self.scrool_lista.configure(
            command=self.listaCLI.yview, troughcolor="#444d46")
        self.listaCLI.configure(yscrollcommand=self.scrool_lista.set)

        self.scrool_lista.pack(fill=Y, expand=True)

        self.listaCLI.bind("<Double-1>", self.OnDubleClick)

        # Aba II - Dados de Estado Civil, Ocupação, Escolaridade e Gênero
        self.listaCLI2 = ttk.Treeview(self.aba2_frame2, height=3, columns=(
            'coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5'))
        self.listaCLI2.heading('#0', text='')
        self.listaCLI2.heading('#1', text='Código')
        self.listaCLI2.heading('#2', text='Estado Civil')
        self.listaCLI2.heading('#3', text='Ocupação')
        self.listaCLI2.heading('#4', text='Escolaridade')
        self.listaCLI2.heading('#5', text='Gênero')

        self.listaCLI2.column('#0', width=1, stretch=NO)
        self.listaCLI2.column('#1', width=80, anchor=CENTER)
        self.listaCLI2.column('#2', width=125, anchor=W)
        self.listaCLI2.column('#3', width=125, anchor=W)
        self.listaCLI2.column('#4', width=150, anchor=W)
        self.listaCLI2.column('#5', width=100, anchor=W)

        self.listaCLI2.place(relx=0.01, rely=0.1,
                             relwidth=0.95, relheight=0.85)

        self.scroll_frame2 = Frame(self.aba2_frame2, bg="#BEBEBE")
        self.scroll_frame2.place(
            relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

        self.scrool_lista2 = Scrollbar(
            self.scroll_frame2, orient='vertical', relief=FLAT, borderwidth=0)
        self.scrool_lista2.configure(
            command=self.listaCLI2.yview, troughcolor="#444d46")
        self.listaCLI2.configure(yscrollcommand=self.scrool_lista2.set)

        self.scrool_lista2.pack(fill=Y, expand=True)

    def Menus(self):
        # Função responsável por criar os menus e suas funcionalidades, na parte superior esquerda: 'Opções, Relatório, Sobre'.
        menuBar = Menu(self.janela)
        self.janela.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu2 = Menu(menuBar)
        fileMenu3 = Menu(menuBar)

        def Quit(): self.janela.destroy()

        def show_creator():
            messagebox.showinfo(
                "Criador", "Este programa foi criado por Luiz Philip Santiago da Silva na data 02/04/2025 enquanto estudava.")

        menuBar.add_cascade(label='Opções', menu=fileMenu)
        menuBar.add_cascade(label='Relatório', menu=fileMenu2)
        menuBar.add_cascade(label='Sobre', menu=fileMenu3)

        fileMenu.add_cascade(label='Limpar Dados', command=self.limpa_tela)
        fileMenu.add_cascade(label='Sair', command=Quit)
        fileMenu2.add_cascade(label='Fichário do Cliente',
                              command=self.gerarRelatCliente)
        fileMenu3.add_cascade(label='Criador', command=show_creator)

    def validaEntradas(self):
        # Função que junto a 'Validadores' atribui uma validação de entrada de dados, nesse caso, na entrada específica de apenas números inteiros na label 'Código'.
        self.validate2 = (self.janela.register(self.validate_entry2), "%P")


Application()