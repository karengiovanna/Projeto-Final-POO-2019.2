from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, Scrollbar, END, Frame, Pack, LEFT, RIGHT, YES, BOTH, VERTICAL
from locacaoDAO import LocacaoDAO
from veiculo import Veiculo
import tkinter.messagebox
import datetime


class Locacao:
    def __init__(self, master=''):

       self.master = master

       self.veiculo = Veiculo()
       self.dao = LocacaoDAO()

       self.preco_produtos = []
       self.lista_compra_final = []

       self.window = Tk()
       self.window.geometry('1350x850+0+0')
       self.window.title('Locar veículo')
       self.window.resizable(0, 0)  # impede de maximizar

       self.left = Frame(self.master, width=800, height=768, bg='#b19cd9')

       self.right = Frame(self.master, width=568, height=768, bg='#c9c9ff')

       self.veiculo_box = Listbox(self.left, width=23, height=21, font=(
       'arial 18 bold'))
       self.veiculo_box.place(x=10, y=80)
       self.scrollbar_veiculo = Scrollbar(self.left)
       self.veiculo_box.configure(yscrollcommand=self.scrollbar_veiculo.set)
       self.scrollbar_veiculo.configure(command=self.veiculo_box.yview)
       self.scrollbar_veiculo.place(x=320, y=80, relheight=0.85, anchor='ne')

       self.pesquisar_veiculo = Label(self.left, text="Pesquisar Produto Por:", font=(
       'arial 18 bold'), bg='white', fg='blue')
       self.pesquisar_veiculo.place(x=10, y=0)

       self.pesquisar_veiculo_nome = Label(self.left, text="Nome:", font=(
       'arial 18 bold'), bg='white', fg='blue')
       self.pesquisar_veiculo_nome.place(x=10, y=40)

       # ID =========================================================
       self.pesquisar_veiculo_id = Label(self.left, text="Id: ", bg='white', fg='blue', font=(
       'arial 18 bold'))
       self.pesquisar_veiculo_id.place(x=350, y=40)
       self.pesquisar_veiculo_id_entry = Entry(self.left, bd='0', bg='lightblue', width=7, font=(
       'arial 18 bold'))
       self.pesquisar_veiculo_id_entry.place(x=390, y=37)

       # BOTAO PESQUISAR =================================================
       self.btn_pesquisa = Button(self.left, text="Pesquisar", width=10, height=1, bg='green', fg='white', font=(
       'arial 11 bold'), command=self.pesquisa)
       self.btn_pesquisa.place(x=500, y=36)

       # TABELA =================================================
       self.veiculo_marca = Label(self.left, text="", bg='white', fg='green', font=(
       'arial 20 bold'))
       self.veiculo_marca.place(x=350, y=120)

       self.veiculo_modelo = Label(self.left, text="", bg='white', fg='green', font=(
       'arial 20 bold'))
       self.veiculo_modelo.place(x=350, y=120)

       self.produto_nome = Label(self.left, text="", bg='white', fg='green', font=(
       'arial 20 bold'))
       self.produto_nome.place(x=350, y=120)

       self.veiculo_diaria = Label(self.left, text="", bg='white', fg='green', font=(
       'arial 20 bold'))
       self.veiculo_diaria.place(x=350, y=160)


       self.c_amount = Label(self.left, text='',
                            font='arial 30 bold', bg='white', fg='red')
       self.c_amount.place(x=350, y=500)

       # pesquisar produto e inserir na list box
       self.pesquisar_veiculo_var = StringVar()
       self.pesquisar_veiculo_var.trace("w", lambda name, index,
                                   mode: self.update_list())
       self.pesquisar_veiculo_nome_entry = Entry(self.left, textvariable=self.pesquisar_veiculo_var, width=16, font=(
       'arial 18 bold'), bd='0', bg='lightblue')
       self.pesquisar_veiculo_nome_entry .place(x=95, y=40)
       self.pesquisar_veiculo_nome_entry.focus()
       self.update_list()

       self.veiculo_box.bind('<<ListboxSelect>>', self.selecionar_linha)

       self.data = Label(self.right, text="      Data de Hoje: " + str(datetime.datetime.now().date()), bg='lightblue', fg='blue', font=(
       'arial 20 bold'))
       self.data.place(x=0, y=0)

       # LEBELS =========================================
       self.produto = Label(self.right, text="Veículo: ", bg='lightblue', fg='blue', font=(
       'arial 18 bold'))
       self.produto.place(x=10, y=50)
       self.quantidade = Label(self.right, text="Diárias: ", bg='lightblue', fg='blue', font=(
       'arial 18 bold'))
       self.quantidade.place(x=180, y=50)
       self.valor = Label(self.right, text="Valor: ", bg='lightblue', fg='blue', font=(
       'arial 18 bold'))
       self.valor.place(x=380, y=50)

       self.total = Label(self.right, text="Valor Total: ", bg='lightblue', fg='blue', font=(
       'arial 27 bold'))
       self.total.place(x=10, y=660)

       self.produto_quantidade = Label(self.left, text="Quantidade: ", bg='white', fg='blue', font=(
       'arial 18 bold'))
       self.produto_quantidade.place(x=350, y=220)
       self.produto_quantidade_entry = Entry(self.left, bd='0', bg='lightblue', width=15, font=(
       'arial 18 bold'))
       self.produto_quantidade_entry.place(x=550, y=220)
       self.produto_quantidade_entry.insert(END, 1)

       self.botao_adicionar = Button(self.left, text="Adicionar", width=10, height=1, bg='blue', fg='white', font=(
       'arial 14 bold'), command=self.adicionar)
       self.botao_adicionar.place(x=582, y=280)

       self.total_pago = Label(self.left, text="Total Pago R$: ", bg='white', fg='blue', font=(
       'arial 18 bold'))
       self.total_pago.place(x=350, y=350)
       self.total_pago_entry = Entry(self.left, bd='0', bg='lightblue', width=15, font=(
       'arial 18 bold'))
       self.total_pago_entry.place(x=550, y=350)

       # self.botao_troco = Button(self.left, text="Troco", width=10, height=1, bg='orange', fg='white', font=(
       #     'arial 18 bold'), command=self.calcular_troco)
       # self.botao_troco.place(x=595, y=400)

       self.botao_recibo = Button(self.left, text="Concluir Venda", width=13, height=1, bg='green', fg='white', font=(
       'arial 16 bold'), command = self.concluir_venda)
       self.botao_recibo.place(x=470, y=630)

       self.venda_box = Listbox(self.right, width=35, height=18, bd='0', font=(
       'arial 18 bold'))
       self.venda_box.place(x=10, y=80)
       self.scrollbar_venda = Scrollbar(self.right)
       self.venda_box.configure(yscrollcommand=self.scrollbar_venda.set)
       self.scrollbar_venda.configure(command=self.venda_box.yview)
       self.scrollbar_venda.place(x=480, y=80, relheight=0.73, anchor='ne')

       self.botao_remover_produto = Button(self.right, text="Remover Produto", width=14, height=1, bg='red', fg='white', font=(
       'arial 14 bold'), command=self.remover_produto_caixa)
       self.botao_remover_produto.place(x=290, y=625)

       self.left.pack(side=LEFT, expand=YES, fill=BOTH)
       self.right.pack(side=RIGHT, expand=YES, fill=BOTH)
    
    def concluir_venda(self):
        if(self.total_pago_entry.get() == ''):
            tkinter.messagebox.showinfo(
                'Supermercado', 'Não foi informado um valor para calcular o troco!')
        else:
            self.to_give = float(self.total_pago_entry.get()) - \
                float(sum(self.preco_produtos))
            if (self.to_give < 0):
                tkinter.messagebox.showinfo(
                    'Supermercado', 'O valor informado é menor que o valor total dos produtos!')
            else:
                self.c_amount.configure(text="Troco R$: " +
                                        str(self.to_give))

                lista_id_quantidade = []
                for item in self.lista_compra_final:
                    temp = []
                    temp.append(item[0])
                    temp.append(item[3])
                    lista_id_quantidade.append(temp)
                
                try:
                    for i in lista_id_quantidade:
                        self.dao.update_estoque(i[1],i[0])
                except:
                    tkinter.messagebox.showinfo(
                    'Supermercado', 'Erro ao acessar o Banco de Dados.')
                else:
                    tkinter.messagebox.showinfo(
                    'Supermercado', 'Venda realizada com sucesso.')
                    
    def limpar_tela(self):
        self.venda_box.delete(0, END)
        self.produto_quantidade_entry.delete(0,END)
        self.pesquisar_veiculo_nome_entry.delete(0,END)
        self.pesquisar_veiculo_id_entry.delete(0,END)
        

    def update_list(self):
        search_term = self.pesquisar_veiculo_var.get()
        try:
            self.veiculo_box.delete(0, END)
            for item in self.dao.view():
                temp = []
                temp.append(item[0])
                temp.append(item[2])
                if str(search_term).lower() in str(temp).lower():
                    self.veiculo_box.insert(END, temp)
        except Exception:
            tkinter.messagebox.showinfo(
                'Supermercado', 'Erro ao acessar o Banco de Dados.')

    def selecionar_linha(self, event):
        if self.veiculo_box.curselection():
            index = self.veiculo_box.curselection()[0]
            self.selected = self.veiculo_box.get(index)
            self.pesquisar_veiculo_id_entry.delete(0, END)
            self.pesquisar_veiculo_id_entry.insert(END, self.selected[0])
            self.produto_quantidade_entry.focus()
            self.pesquisa()

    def remover_produto_caixa(self):
        if self.venda_box.curselection():
            index = self.venda_box.curselection()[0]
            self.venda_box.delete(index)
            del self.preco_produtos[index]
            self.total.configure(
                text="Valor Total R$: " + str(sum(self.preco_produtos)))
            self.lista_compra_final = self.venda_box.get(0, END)

    def pesquisa(self):
        self.get_id = self.pesquisar_veiculo_id_entry.get()

        result = self.dao.view_venda(self.pesquisar_veiculo_id_entry.get())

        for self.r in result:
            self.get_id = self.r[0]
            self.get_nome = self.r[1]
            self.get_valor_venda = self.r[2]
            self.get_quantidade = self.r[3]

        self.veiculo_marca.configure(text="Marca: " + str(self.get_nome))
        self.veiculo_diaria.configure(
            text="Diária R$: " + str(self.get_valor_venda))

    def adicionar(self):
        try:
            self.valor_quantidade = int(self.produto_quantidade_entry.get())
            if(self.valor_quantidade > int(self.get_quantidade)):
                tkinter.messagebox.showinfo(
                    'Supermercado', 'Quantidade acima do disponível no estoque.')
            else:
                self.preco_final = (
                    float(self.valor_quantidade * self.get_valor_venda))
                produto_lista = []
                produto_lista.append(self.get_id)
                produto_lista.append(self.get_marca)
                produto_lista.append(str('--------------'))
                produto_lista.append(self.valor_diaria)
                produto_lista.append(str('--------------'))
                produto_lista.append(self.preco_final)

                self.preco_produtos.append(self.preco_final)

                self.venda_box.insert(END, produto_lista)
                self.lista_compra_final = self.venda_box.get(0, END)

                self.total.configure(
                    text="Valor Total R$: " + str(sum(self.preco_produtos)))
        except AttributeError:
            tkinter.messagebox.showinfo(
                'Supermercado', 'Selecione um produto antes de adicionar a lista!')

    #def calcular_troco(self):
       

    def run(self):
        self.window.mainloop()

Locacao().run()