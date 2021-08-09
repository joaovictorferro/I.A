import tkinter as tk
from PIL import ImageTk
import regrasRecomendacao as rules
from experta import Fact
import tkinter.font as tkFont

#Busca nas regras qual recomendacao foi redirecionada    
def detectarRecomendacao():    
    sistemaEspecialista = rules.RegrasRecomendacao()
    sistemaEspecialista.reset()

    sistemaEspecialista.declare(Fact(tipoRam = str(escolhaTipoRam.get())))
    sistemaEspecialista.declare(Fact(tipoPreco = str(escolhaPreco.get())))
    sistemaEspecialista.declare(Fact(tipoMultiChip = str(escolhaTipoMultichip.get())))
    sistemaEspecialista.declare(Fact(capacidade = str(escolhaCapacidade.get())))
    sistemaEspecialista.declare(Fact(camFrontal = str(escolhaCamFrontal.get())))
    sistemaEspecialista.declare(Fact(camPrincipal = str(escolhaCamPrincipal.get())))
    sistemaEspecialista.declare(Fact(marca = str(escolhaMarca.get())))

    sistemaEspecialista.run()
    
    celularRecomendado.config(state = tk.NORMAL)
    precoCelular.config(state = tk.NORMAL)
    
    celularRecomendado.delete("1.0", "end")
    celularRecomendado.insert(tk.INSERT, sistemaEspecialista.carro)
    precoCelular.delete("1.0", "end")
    precoCelular.insert(tk.INSERT, sistemaEspecialista.precodoCarro)
    
    celularRecomendado.config(state = tk.DISABLED)
    precoCelular.config(state = tk.DISABLED)

#Limpando os campos utilizados
def limpar():
    celularRecomendado.config(state = tk.NORMAL)
    precoCelular.config(state = tk.NORMAL)
    
    celularRecomendado.delete("1.0", "end")
    precoCelular.delete("1.0", "end")
    
    celularRecomendado.config(state = tk.DISABLED)
    precoCelular.config(state = tk.DISABLED)
    
    escolhaTipoRam.set(None)
    escolhaPreco.set(None)
    escolhaTipoMultichip.set(None)
    escolhaCapacidade.set(None)
    escolhaCamFrontal.set(None)
    escolhaCamPrincipal.set(None)
    escolhaMarca.set(None)


background = "#99f6ff"
raiz = tk.Tk()
raiz.title("Escolha de Celular")
#raiz.geometry("+250+0")
raiz.config(bg=background)
raiz.resizable(True, True)

#variaveis de escolha dos campos selecionados
escolhaTipoRam = tk.IntVar()    
escolhaPreco = tk.IntVar()    
escolhaTipoMultichip = tk.IntVar()
escolhaCapacidade = tk.IntVar() 
escolhaCamFrontal = tk.IntVar() 
escolhaCamPrincipal = tk.IntVar() 
escolhaMarca = tk.IntVar()


#interface do programa (iniciando com o titulo)
fontStyle = tkFont.Font(family="Helvetica", size=20, weight="bold")
l1 = tk.Label(raiz, text="Marque as opções que você deseja", width=30, bg=background,  font=fontStyle)
l1.grid(row = 0, column = 1, pady = 5, padx=5 )

#Titulo Faixa de Preço
fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Faixa de Preço", width=60, bg=background, font=fontTipo).grid(row = 1, column = 1, pady = 5)

#caixa de selecao menos que R$2000
c1 = tk.Checkbutton(raiz, text = "Menos que R$ 2000,00", variable= escolhaPreco, onvalue=2 ,offvalue=0,width=50, height=5, bg= background)
c1.grid(row = 2, column = 0)

#caixa de selecao mais que R$2000 e menos que R$5000
c1 = tk.Checkbutton(raiz, text = "Entre R$2000,00 e R$ 5000,00", variable= escolhaPreco, onvalue=25 ,offvalue=0,width=50, height=5, bg= background)
c1.grid(row = 2, column = 1)

#caixa de selecao mais que R$5000
c1 = tk.Checkbutton(raiz, text = "Mais que R$ 5000,00", variable= escolhaPreco, onvalue=5 ,offvalue=0,width=50, height=5, bg= background)
c1.grid(row = 2, column = 2)

#Titulo da Ram
fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Ram", width=60, bg=background, font=fontTipo).grid(row = 3, column = 1)

#caixa de selecao do tipo 2GB de Ram
c1 = tk.Checkbutton(raiz, text = "2 GB", variable= escolhaTipoRam, onvalue=2 ,offvalue=0,width=5, height=5, bg= background)
c1.grid(row = 4, column = 0)

#caixa de selecao do tipo 3GB de Ram
c2 = tk.Checkbutton(raiz, text = "3 GB", variable = escolhaTipoRam, onvalue=3 ,offvalue=0,width=5, height=5, bg= background)
c2.grid(row = 4, column = 1)

#caixa de selecao do tipo 4GB de Ram
c3 = tk.Checkbutton(raiz, text = "4 GB", variable = escolhaTipoRam, onvalue=4 ,offvalue=0,width=5, height=5, bg=background)
c3.grid(row = 4, column = 2)

#caixa de selecao do tipo 6GB de Ram
c4 = tk.Checkbutton(raiz, text = "6 GB", variable = escolhaTipoRam, onvalue=6,offvalue=0,width=5, height=5, bg=background)
c4.grid(row = 5, column = 0)

#caixa de selecao do tipo 8GB de Ram
c5 = tk.Checkbutton(raiz, text = "8 GB", variable = escolhaTipoRam, onvalue=8 ,offvalue=0,width=5, height=5, bg=background)
c5.grid(row = 5, column = 1)

#caixa de selecao do tipo 12GB de Ram
c6 = tk.Checkbutton(raiz, text = "12 GB", variable = escolhaTipoRam, onvalue=12 ,offvalue=0,width=3, height=5, bg=background)
c6.grid(row = 5, column = 2)

#Titulo Capacidade do celular
tk.Label(raiz, text="Capacidade do Celular", width=60, bg=background, font=fontTipo).grid(row = 6, column = 1, pady = 5)

#caixa de selecao do tipo 64B de Ram
c6 = tk.Checkbutton(raiz, text = "64 GB", variable = escolhaCapacidade, onvalue=64 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 0)

#caixa de selecao do tipo 12GB de Ram
c6 = tk.Checkbutton(raiz, text = "128 GB", variable = escolhaCapacidade, onvalue=128 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 1)

#Titulo Marca do Celular
tk.Label(raiz, text="Marca do Celular", width=60, bg=background, font=fontTipo).grid(row = 8, column = 1, pady = 5)

#caixa de selecao da Apple
c6 = tk.Checkbutton(raiz, text = "Apple", variable = escolhaCapacidade, onvalue=1 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 0)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "LG", variable = escolhaCapacidade, onvalue=2,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 1)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "ASUS", variable = escolhaCapacidade, onvalue=3,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 2)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "Motorola", variable = escolhaCapacidade, onvalue=4,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 0)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "Samsung", variable = escolhaCapacidade, onvalue=5,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 1)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "Xiomi", variable = escolhaCapacidade, onvalue=6,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 2)

#Titulo Capacidade do celular
tk.Label(raiz, text="Capacidade do Celular", width=60, bg=background, font=fontTipo).grid(row = 6, column = 1, pady = 5)

#caixa de selecao do tipo 64B de Ram
c6 = tk.Checkbutton(raiz, text = "64 GB", variable = escolhaCapacidade, onvalue=64 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 0)

#caixa de selecao do tipo 12GB de Ram
c6 = tk.Checkbutton(raiz, text = "128 GB", variable = escolhaCapacidade, onvalue=128 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 1)


#loop da main para funcionamento do aplicativo
raiz.mainloop()