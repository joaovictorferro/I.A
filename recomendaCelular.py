import tkinter as tk
from PIL import ImageTk, Image
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

    return sistemaEspecialista.celular, sistemaEspecialista.precodoCelular, sistemaEspecialista.imagem


def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel()

    # sets the title of the
    # Toplevel widget
    newWindow.title("Recomendacao")

    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    # A Label widget to show in toplevel
    tk.Label(newWindow, text ="Este e seu celular").pack()

    celularRecomendado, precoCelular, caminhoImagem = detectarRecomendacao() 

    if celularRecomendado == precoCelular == caminhoImagem == '':
        celularRecomendado = 'Infelizmente não temos um celular que se enquadre nos seus desejos.'
        caminhoImagem = r'.\Fotos\question.jpg'

    img = ImageTk.PhotoImage(Image.open(caminhoImagem).resize((200, 200)))

    canvas = tk.Canvas (newWindow, width = 300, height = 300)
    canvas.pack()
    canvas.create_image(120, 120, anchor = tk.CENTER, image=img)
    canvas.img = img
    
    # A Label celular Recomendado
    tk.Label(newWindow, text =str(celularRecomendado)).pack()

    # A Label Preco do celular
    tk.Label(newWindow, text =str(precoCelular)).pack()

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
l1.grid(row = 0, column = 1, pady = 0, padx=5 )

#Titulo Faixa de Preço
fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Faixa de Preço", width=60, bg=background, font=fontTipo).grid(row = 1, column = 1, pady = 0)

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
tk.Label(raiz, text="Capacidade do Celular", width=60, bg=background, font=fontTipo).grid(row = 6, column = 1, pady = 0)

#caixa de selecao do tipo 32GB de Ram Secundaria
c6 = tk.Checkbutton(raiz, text = "32 GB", variable = escolhaCapacidade, onvalue=32 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 0)

#caixa de selecao do tipo 64GB de Ram Secundaria
c6 = tk.Checkbutton(raiz, text = "64 GB", variable = escolhaCapacidade, onvalue=64 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 1)

#caixa de selecao do tipo 128GB de Ram Secundaria
c6 = tk.Checkbutton(raiz, text = "128 GB", variable = escolhaCapacidade, onvalue=128 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 7, column = 2)

#Titulo Marca do Celular
tk.Label(raiz, text="Marca do Celular", width=60, bg=background, font=fontTipo).grid(row = 8, column = 1, pady = 0)

#caixa de selecao da Apple
c6 = tk.Checkbutton(raiz, text = "Apple", variable = escolhaMarca, onvalue=1 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 0)

#caixa de selecao da LG
c6 = tk.Checkbutton(raiz, text = "LG", variable = escolhaMarca, onvalue=2,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 1)

#caixa de selecao da ASUS
c6 = tk.Checkbutton(raiz, text = "ASUS", variable = escolhaMarca, onvalue=3,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 9, column = 2)

#caixa de selecao da MOTOROLA
c6 = tk.Checkbutton(raiz, text = "Motorola", variable = escolhaMarca, onvalue=4,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 0)

#caixa de selecao da SAMSUNG
c6 = tk.Checkbutton(raiz, text = "Samsung", variable = escolhaMarca, onvalue=5,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 1)

#caixa de selecao da XIOMI
c6 = tk.Checkbutton(raiz, text = "Xiomi", variable = escolhaMarca, onvalue=6,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 10, column = 2)

#Titulo Cam Frontal ou Principal
tk.Label(raiz, text="Cam Frontal ou Principal", width=60, bg=background, font=fontTipo).grid(row = 11, column = 1, pady = 0)

#caixa de selecao do tipo CAM Frontal
c6 = tk.Checkbutton(raiz, text = "CAM Frontal", variable = escolhaCamFrontal, onvalue=1 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 12, column = 0)

#caixa de selecao do tipo CAM Principal
c6 = tk.Checkbutton(raiz, text = "CAM Principal", variable = escolhaCamPrincipal, onvalue=2 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row =12, column = 1)

#Titulo MULTICHIP
tk.Label(raiz, text="Multichip", width=60, bg=background, font=fontTipo).grid(row = 13, column = 1, pady = 0)

#caixa de selecao do tipo 1 Chip
c6 = tk.Checkbutton(raiz, text = "1 Chip", variable = escolhaTipoMultichip, onvalue=1 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row = 14, column = 0)

#caixa de selecao do tipo 2 Chip
c6 = tk.Checkbutton(raiz, text = "2 Chip", variable = escolhaTipoMultichip, onvalue=2 ,offvalue=0,width=20, height=5, bg=background)
c6.grid(row =14, column = 1)

#caixa Confirmar
b1 = tk.Button(raiz, text="Confirmar", command = openNewWindow, bg=background)
b1.grid(row = 15, column = 1, padx = 10, pady=0)

#loop da main para funcionamento do aplicativo
raiz.mainloop()