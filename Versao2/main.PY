from tkinter import Tk, Frame, Button, Menu
from veiculo.cadastrar_veiculo import CadastroVeiculo
# from veiculo..atualizar_veiculo import AtualizaVeiculo
#from veiculo.delete_veiculo import DeleteVeiculo
#from fornecedor.fornecedor_cadastro import FornecedorCadastro
#from fornecedor.fornecedor_atualizar import FornecedorAtualizar
#from fornecedor.fornecedor_deletar import FornecedorDeletar
#from locacao.locacao import Locacao

class Main(Frame):
    def __init__(self, *args, **kwargs):
       Frame.__init__(self, master=None)

       # Configuração da janela principal
       self.master.title('Bem-vindo ao sistema de locação de carros')
       self.master.geometry('1280x720+0+0')
       # Impede de maximizar
       self.master.resizable(0, 0)  

       self.menubar = Menu(self.master, bg='lightblue')
       self.master.configure(menu=self.menubar)
       self.menu_veiculo = Menu(self.menubar)
       self.menu_cliente = Menu(self.menubar)
       #self.menu_fornecedor = Menu(self.menubar)
       self.menu_locacao = Menu(self.menubar)

       self.menubar.add_cascade(label='Veiculo  ', font=(
       'arial 20 bold'), menu=self.menu_veiculo)
       self.menubar.add_cascade(label='Cliente  ', font=(
       'arial 20 bold'), menu=self.menu_cliente)
       '''self.menubar.add_cascade(label='Fornecedor  ', font=(
       'arial 20 bold'), menu=self.menu_fornecedor)
       '''
       self.menubar.add_cascade(label='Caixa ', font=(
       'arial 20 bold'), menu=self.menu_locacao)

       self.menu_veiculo.add_command(label='Cadastrar Veiculo', font=(
       'arial 18 bold'), command=self.cadastrar_veiculo)
       '''self.menu_veiculo.add_command(label='Atualizar Veiculo', font=(
       'arial 18 bold'), command=self.veiculo)
       '''
       self.menu_veiculo.add_command(label='Deletar Veiculo', font=(
       'arial 18 bold'), command=self.deletar_produto)

       self.menu_cliente.add_command(label='Cadastrar Cliente', font=(
       'arial 18 bold'))
       self.menu_cliente.add_command(label='Atualizar Cliente', font=(
       'arial 18 bold'))
       self.menu_cliente.add_command(label='Deletar Cliente', font=(
       'arial 18 bold'))

       '''
       self.menu_fornecedor.add_command(label='Cadastrar Fornecedor', font=(
       'arial 18 bold'), command= self.cadastrar_fornecedor)
       self.menu_fornecedor.add_command(label='Atualizar Fornecedor', font=(
       'arial 18 bold'), command= self.atualizar_fornecedor)
       self.menu_fornecedor.add_command(label='Deletar Fornecedor', font=(
       'arial 18 bold'), command= self.deletar_fornecedor)
       '''

       self.menu_locacao.add_command(label='Realizar locacao', font=(
       'arial 18 bold'), command = self.realizar_locacao)

       self.configure(borderwidth=4)
       self.configure(background='lightblue')

       # Empacotamos o frame principal
       self.pack(fill='both', expand=True)

       def cadastrar_veiculo(self):
              CadastroVeiculo().run()
       '''
       def atualizar_veiculo(self):
              ProdutoAtualiza().run()
       '''
       def deletar_veiculo(self):
              DeleteVeiculo().run()
       '''
       def cadastrar_fornecedor(self):
              FornecedorCadastro().run()

       def atualizar_fornecedor(self):
              FornecedorAtualizar().run()

       def deletar_fornecedor(self):
              FornecedorDeletar().run()
       '''
       def realizar_locacao(self):
              Locacao().run()


if __name__ == '__main__':
    mainWindow = Main()
    mainWindow.mainloop()
