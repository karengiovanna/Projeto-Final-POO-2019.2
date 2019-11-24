from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, END
from clienteDAO import ClienteDAO
from cliente import Cliente
import tkinter.messagebox
import datetime

class CadastroCliente:
    '''Classe interface cadastrar cliente'''

    def __init__(self, master=''):
        self.master = master
        self.cliente = Cliente()
        self.dao = ClienteDAO()
        '''
        self.window = Tk()
        self.window.geometry('1500x850+0+0')
        self.window.title('Cadastro de cliente')
        self.window.resizable(0, 0)  # impede de maximizar
        self.window['bg'] = '#c9c9ff'
        '''
        self.heading = Label(self.master, text="Cadastro de Clientes", bg='#c9c9ff', fg='white', font=(
        'Verdana 20 bold'))
        self.heading.place(x=650, y=0)

        # nome ========================================================================= 
        self.nome = Label(self.master, text="Nome:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.nome.place(x=30, y=70)
        self.nome_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.nome_entry.place(x=175, y=70)

        # rg ========================================================================= 
        self.rg = Label(self.master, text="rg:", bg='#c9c9ff',fg='white', font=(
        'Verdana 15 bold'))
        self.rg.place(x=30, y=120)
        self.rg_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.rg_entry.place(x=175, y=120)

        # cpf ========================================================================= 
        self.cpf = Label(self.master, text="cpf:", bg='#c9c9ff',fg='white', font=(
        'Verdana 15 bold'))
        self.cpf.place(x=30, y=170)
        self.cpf_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.cpf_entry.place(x=175, y=170)

        # email ========================================================================= 
        self.email = Label(self.master, text="email:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.email.place(x=30, y=220)
        self.email_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.email_entry.place(x=175, y=220)
        # self.email_entry.insert(END, datetime.date.today())

        # telefone ========================================================================= 
        self.telefone = Label(self.master, text="Telefone:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.telefone.place(x=30, y=270)
        self.telefone_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.telefone_entry.place(x=175, y=270)
        self.telefone_entry.insert(END, "litros")



        # nascimento ========================================================================= 
        self.nascimento = Label(self.master, text="Nascimento:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.nascimento.place(x=30, y=320)
        self.nascimento_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.nascimento_entry.place(x=175, y=320)

        # consumo cidade ========================================================================= 
        self.estado_civil = Label(self.master, text="Estado civil:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.estado_civil.place(x=30, y=370)
        self.estado_civil_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.estado_civil_entry.place(x=175, y=370)
        
        self.estado_civil_entry.insert(END, "l/km")

        
        self.genero = Label(self.master, text="Gênero:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.genero.place(x=30, y=420)
        self.genero_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.genero_entry.place(x=175, y=420)
        self.genero_entry.insert(END, "l/km")
        
        # direito ==============================
        self.cep = Label(self.master, text="CEP:", bg='#c9c9ff',fg='white',  font=(
        'Verdana 15 bold'))
        self.cep.place(x=550, y=70)
        self.cep_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.cep_entry.place(x=730, y=70)



        self.estado = Label(self.master, text="Estado:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.estado.place(x=550, y=120)
        self.estado_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.estado_entry.place(x=730, y=120)


        self.logradouro = Label(self.master, text="Logradouro:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.logradouro.place(x=550, y=170)
        self.logradouro_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.logradouro_entry.place(x=730, y=170)


        self.bairro = Label(self.master, text="Bairro:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.bairro.place(x=550, y=220)
        self.bairro_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.bairro_entry.place(x=730, y=220)


        self.numero_logradouro = Label(self.master, text="Número:", bg='#c9c9ff', fg='white',  font=(
        'Verdana 15 bold'))
        self.numero_logradouro.place(x=550, y=270)
        self.numero_logradouro_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.numero_logradouro_entry.place(x=730, y=270)

        self.cidade = Label(self.master, text="Cidade:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.cidade.place(x=550, y=320)
        self.cidade_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.cidade_entry.place(x=730, y=320)

        self.complemento = Label(self.master, text="Complemento:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.complemento.place(x=550, y=370)
        self.complemento_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.complemento_entry.place(x=730, y=370)

        # TERCEIRO FRAME =============================================
        self.numero_cnh = Label(self.master, text="Numero CNH:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.numero_cnh.place(x=1050, y=70)
        self.numero_cnh_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.numero_cnh_entry.place(x=1250, y=70)

        self.numero_registro_cnh = Label(self.master, text="RG CNH:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.numero_registro_cnh.place(x=1050, y=120)
        self.numero_registro_cnh_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.numero_registro_cnh_entry.place(x=1250, y=120)

        self.data_validade_cnh = Label(self.master, text="Validade CNH:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.data_validade_cnh.place(x=1050, y=170)
        self.data_validade_cnh_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.data_validade_cnh_entry.place(x=1250, y=170)

        self.uf_cnh = Label(self.master, text="UF CNH:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.uf_cnh.place(x=1050, y=220)
        self.uf_cnh_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.uf_cnh_entry.place(x=1250, y=220)

        self.contato_emergencial = Label(self.master, text="Contato 2:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.contato_emergencial.place(x=1050, y=270)
        self.contato_emergencial_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.contato_emergencial_entry.place(x=1250, y=270)

        self.nome_contato_emergencial = Label(self.master, text="Nome contato:", bg='#c9c9ff', fg='white', font=(
        'Verdana 15 bold'))
        self.nome_contato_emergencial.place(x=1050, y=320)
        self.nome_contato_emergencial_entry = Entry(self.master, width=15, font=(
        'Verdana 15 bold'))
        self.nome_contato_emergencial_entry.place(x=1250, y=320)
        
        # BOTAO LIMPAR  ========================================================================= 
        self.botao_limpar = Button(self.master, text="Limpar", width=22, height=2, bg='#ffdfba', fg='black', font=(
        'Verdana 15 bold'), command=self.view_command)
        self.botao_limpar.place(x=1170, y=550)

        self.botao_cadastrar = Button(self.master, text="Cadastrar", width=22, height=2, bg='#baffc9', fg='black', font=(
        'Verdana 15 bold'), command=self.get_items)
        self.botao_cadastrar.place(x=1170, y=650)
        '''
        self.botao_sair = Button(self.master, text="Sair", width=22, height=2, bg='#ffb3ba', fg='black', font=(
        'Verdana 15 bold'), command=self.close)
        self.botao_sair.place(x=1170, y=740)
        '''
        self.lista_clientes = Listbox(self.master, width=80, height=10, font=(
        'Verdana 15 bold'))
        self.lista_clientes.place(x=30, y=550)

        #Associando a Scrollbar com a Listbox...
        self.scrollbar_cliente = Scrollbar(self.master)
        self.lista_clientes.configure(yscrollcommand=self.scrollbar_cliente.set)
        self.scrollbar_cliente.configure(command=self.lista_clientes.yview)
        self.scrollbar_cliente.place(x=1155, y=550, relheight=0.31, anchor='ne')

        self.pesquisar_cliente = Label(self.master, text="Lista de clientes Cadastrados:", bg='#c9c9ff',  font=(
        'Verdana 15 bold'))
        self.pesquisar_cliente.place(x=30, y=500)
        self.update_list()

    def update_list(self):
        try:
            self.lista_clientes.delete(0, END)
            for item in self.clienteDAO.view():
                self.lista_clientes.insert(END, item)
        except Exception:
            print('Erro na lista clientes.')

    def get_items(self):
        self.cliente.nome = self.nome_entry.get()
        self.cliente.rg = self.rg_entry.get()
        self.cliente.cpf = self.cpf_entry.get()
        self.cliente.email = self.email_entry.get()
        self.cliente.telefone = self.telefone_entry.get()
        self.cliente.nascimento = self.nascimento_entry.get()
        self.cliente.estado_civil = self.estado_civil_entry.get()
        self.cliente.genero = self.genero_entry.get()
        self.cliente.cep = self.cep_entry.get()
        self.cliente.logradouro = self.logradouro_entry.get()
        self.cliente.bairro = self.bairro_entry.get()
        self.cliente.numero_logradouro = self.numero_logradouro_entry.get()
        self.cliente.cidade = self.cidade_entry.get()
        self.cliente.estado = self.estado_entry.get()
        self.cliente.complemento = self.complemento_entry.get()
        self.cliente.numero_cnh = self.numero_cnh_entry.get()
        self.cliente.numero_registro_cnh = self.numero_registro_cnh_entry.get()
        self.cliente.data_validade_cnh = self.data_validade_cnh_entry.get()
        self.cliente.uf_cnh = self.uf_cnh_entry.get()
        self.cliente.contato_emergencial = self.contato_emergencial_entry.get()
        self.cliente.nome_contato_emergencial = self.nome_contato_emergencial_entry.get()

        if(self.cliente.nome == '' or self.cliente.rg == '' or self.cliente.cpf == '' or self.cliente.email == '' or self.cliente.telefone == '' or self.cliente.nascimento == '' or self.cliente.estado_civil == '' or self.cliente.genero == '' or self.cliente.cep == '' or self.cliente.logradouro == '' or self.cliente.bairro == '' or self.cliente.numero_logradouro == '' or self.cliente.cidade == '' or self.cliente.estado == '' or self.cliente.complemento == '' or self.cliente.numero_cnh == '' or self.cliente.numero_registro_cnh == '' or self.cliente.data_validade_cnh == '' or self.cliente.uf_cnh == '' or self.cliente.contato_emergencial == '' or self.cliente.nome_contato_emergencial == ''):
            tkinter.messagebox.showinfo(
                "Aviso:", "Preencha todos os campos!")
        else:
            try:
                self.cliente.telefone = int(self.cliente.telefone)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo telefone deve ser preenchido com número!')
            try:
                self.cliente.contato_emergencial = int(self.cliente.contato_emergencial)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo contato emergencial deve ser preenchidos com número!')
            try:
                self.cliente.cep = int(self.cliente.cep)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo cep deve ser preenchido com números!')
            try:
                self.cliente.numero_cnh = int(self.cliente.numero_cnh)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo numero cnh deve ser preenchido com números!')               
            try:    
                self.cliente.numero_registro_cnh = int(self.cliente.numero_registro_cnh)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo rg cnh deve ser preenchido com números!')    
            try: 
                self.cliente.uf_cnh = int(self.cliente.uf_cnh)
            except ValueError:
                tkinter.messagebox.showinfo(
                    'Aviso!', 'O campo uf cnh deve ser preenchido com números!!')
            else:
                try:
                    self.dao.insert(self.cliente)
                except Exception as e:
                    print("erro ao inserir no banco de dados")
                else:
                    tkinter.messagebox.showinfo(
                        'Aviso!', 'Cadastro Realizado com Sucesso!')
                    self.clear_all()
                    self.update_list()

    def clear_all(self):
        self.nome_entry.delete(0, END)
        self.rg_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.nascimento_entry.delete(0, END)
        self.estado_civil_entry.delete(0, END)
        self.genero_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.logradouro_entry.delete(0, END)
        self.bairro.delete(0, END)
        self.numero_logradouro.delete(0, END)
        self.cidade.delete(0, END)
        self.estado.delete(0, END)
        self.complemento.delete(0, END)
        self.numero_cnh.delete(0, END)
        self.numero_registro_cnh.delete(0, END)
        self.data_validade_cnh.delete(0, END)
        self.uf_cnh.delete(0, END)
        self.contato_emergencial.delete(0, END)
        self.nome_contato_emergencial.delete(0, END)

    def view_command(self):
        "método para visualização dos resultados"
        try:
            rows = self.clienteDAO.view()
            self.window.lista_clientes.delete(0, END)
            for r in rows:
                self.window.lista_clientes.insert(END, r)
        except Exception as e:
            print(e)
    
    def search_command(self):
        "método para buscar registros"
        self.gui.lista_clientes.delete(0, END)
        self.__fill_current_client()
        try:
            rows = self.dao.search(self.currentClient)
            for r in rows:
                self.gui.lista_clientes.insert(END, r)
        except Exception as e:
            print(e)

    def close(self):
        self.dao.close()
        self.tela_inicial.destroy()
        self.executar.abrir()

    #def run(self):
        #self.tela_inicial.mainloop()


#CadastroCliente().run()
