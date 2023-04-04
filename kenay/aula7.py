import tkinter as tk

class janela:
    def __init__(self, toplevel):
        self.fr1 =tk.Frame(toplevel)
        self.fr1.grid(column=4, row=4)
        
        self.texto =tk.Label(text='informe seu nome: ')
        self.texto.grid(column=4, row=1)

        self.bt = tk.Button(text='BOTÃO', background='#ffffff', command=self.abrijanela)
        self.bt.grid(column=2, row=4)
        

        self.campo = tk.Entry(font=10, width=50)
        self.campo.grid(column=2, row=1)

    def imprimir(self):

        print('###')
        print(self.campo.get())

    def abrijanela(self):
        jn = tk.Toplevel()
        jn,title('teste nova janela')
        jn.geometry('500x500')
         


raiz = tk.Tk()
raiz.geometry('500x500')
raiz.title('Sign in')
janela(raiz)
raiz.mainloop()





