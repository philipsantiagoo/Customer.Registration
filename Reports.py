from bibliotecas import *


# FrontEND
class Relatórios():
    def printCliente(self):
        # Faz exibir e salvar o arquivo, chamando a função abaixo [ PDF ]
        webbrowser.open('cliente.pdf')

    def gerarRelatCliente(self):
        # Faz o pdf de cada cliente salvo
        self.c = canvas.Canvas('cliente.pdf')

        self.códigoRel = self.código.get()
        self.nomeRel = self.nome.get()
        self.telefoneRel = self.telefone.get()
        self.cidadeRel = self.cidade.get()

        self.c.setFont('Helvetica-Bold', 10)
        self.c.drawString(245, 790, '<< Ficha do Cliente >>')

        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(50, 745, 'Código: ')
        self.c.drawString(50, 733, 'Nome: ')
        self.c.drawString(50, 721, 'Telefone: ')
        self.c.drawString(50, 709, 'Cidade: ')

        # Ainda terão suas funcionalidades criadas:
        self.c.drawString(50, 688, 'Estado Civil: ')
        self.c.drawString(50, 676, 'Ocupação: ')
        self.c.drawString(50, 664, 'Escolaridade: ')
        self.c.drawString(50, 652, 'Gênero: ')

        self.c.setFont("Helvetica", 8)
        self.c.drawString(110, 745, self.códigoRel)
        self.c.drawString(110, 733, self.nomeRel)
        self.c.drawString(110, 721, self.telefoneRel)
        self.c.drawString(110, 709, self.cidadeRel)

        # Ainda terão suas funcionalidades criadas:
        # self.c.drawString(110, 697, self.estadocivilRel)
        # self.c.drawString(110, 685, self.ocupacaoRel)
        # self.c.drawString(110, 673, self.escolaridadeRel)
        # self.c.drawString(110, 661, self.generoRel)

        self.c.showPage()
        self.c.save()
        self.printCliente()