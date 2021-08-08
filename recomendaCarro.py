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

#Titulo da Ram
fontTipo = tkFont.Font(family="Helvetica", size=15)
tk.Label(raiz, text="Ram", width=60, bg=background, font=fontTipo).grid(row = 1, column = 1, pady = 5)

#caixa de selecao do tipo 2GB de Ram
c1 = tk.Checkbutton(raiz, text = "2 GB", variable= escolhaTipoRam, onvalue=2 ,width=5, height=5, bg= background)
c1.grid(row = 2, column = 0, pady = 5)
print(escolhaTipoRam.get())

#caixa de selecao do tipo 3GB de Ram
c2 = tk.Checkbutton(raiz, text = "3 GB", variable = escolhaTipoRam, onvalue=3 ,width=5, height=5, bg= background)
c2.grid(row = 2, column = 1, pady = 5)

#caixa de selecao do tipo 4GB de Ram
c3 = tk.Checkbutton(raiz, text = "4 GB", variable = escolhaTipoRam, onvalue=4 ,width=5, height=5, bg=background)
c3.grid(row = 2, column = 2, pady = 5)

#caixa de selecao do tipo 6GB de Ram
c4 = tk.Checkbutton(raiz, text = "6 GB", variable = escolhaTipoRam, onvalue=6 ,width=5, height=5, bg=background)
c4.grid(row = 3, column = 0, pady = 5)

#caixa de selecao do tipo 8GB de Ram
c5 = tk.Checkbutton(raiz, text = "8 GB", variable = escolhaTipoRam, onvalue=8 ,width=5, height=5, bg=background)
c5.grid(row = 3, column = 1, pady = 5)

#caixa de selecao do tipo 12GB de Ram
c6 = tk.Checkbutton(raiz, text = "12 GB", variable = escolhaTipoRam, onvalue=12 ,width=3, height=5, bg=background)
c6.grid(row = 3, column = 2, pady = 5)

#Titulo motor do carro
tk.Label(raiz, text="Motor do carro", width=60, bg=background, font=fontTipo).grid(row = 4, column = 1, pady = 5)

#caixa de selecao do Motor 1.0 Turbo
# img4 = ImageTk.PhotoImage(file = "./fotos/capacidade.jpg")
c4 = tk.Checkbutton(raiz, text = "Motor 1.0 turbo", variable = escolhaCapacidade,  width=100, height=100, bg=background)
c4.grid(row = 4, column = 0, pady = 5)

#caixa de selecao do Motor 1.4 turbo
# img5 = ImageTk.PhotoImage(file = "./fotos/motor1.4t.jpg")
c5= tk.Checkbutton(raiz, text = "Motor 1.4 turbo", variable = escolhaCamFrontal,  width=100, height=100, bg=background)
c5.grid(row = 4, column = 1, pady = 5)

#caixa de selecao do Motor 2.0 turbo
# img6 = ImageTk.PhotoImage(file = "./fotos/camPrincipal.jpg")
c6 = tk.Checkbutton(raiz, text = "Motor 2.0 turbo", variable = escolhaCamPrincipal,  width=100, height=100, bg=background)
c6.grid(row = 4, column = 2, pady = 5) 

#Titulo cambio do carro
tk.Label(raiz, text="Cambio do carro", width=60, bg=background, font=fontTipo).grid(row = 5, column = 1, pady = 5)

#caixa de selecao do cambio marca
# img7 = ImageTk.PhotoImage(file = "./fotos/cambio-marca.jpg")
c7 = tk.Checkbutton(raiz, text = "marca", variable = escolhaMarca,  width=100, height=100, bg=background)
c7.grid(row = 6, column = 0, padx= 10, pady = 10)

"""
#caixa de selecao do cambio automatico
# img8 = ImageTk.PhotoImage(file = "./fotos/cambio-automatico.jpg")
c8 = tk.Checkbutton(raiz, text = "Automatico", variable = escolhaAutomatico,  width=100, height=110, compound='top',bg=background)
c8.grid(row = 6, column = 1, padx=10, pady = 10)

#Titulo opcionais do carro
tk.Label(raiz, text="Opcionais do carro", width=60, bg=background, font=fontTipo).grid(row = 7, column = 1, pady = 5)

#caixa de selecao do Ar condicionado
# img9 = ImageTk.PhotoImage(file = "./fotos/ar_condicionado.jpg")
c9 = tk.Checkbutton(raiz, text = "Ar condicionado", variable = escolhaAr_condicionado,  width=100, height=100, compound='top', bg=background)
c9.grid(row = 8, column = 2, pady = 5)

#caixa de selecao do Farol de milha
# img10 = ImageTk.PhotoImage(file = "./fotos/farol_de_milha.jpg")
c10 = tk.Checkbutton(raiz, text = "Farol de milha", variable = escolhaFarol_de_milha,  width=100, height=110, compound='top', bg=background)
c10.grid(row = 8, column = 0, pady = 5)

#caixa de selecao do Camera de re
# img11 = ImageTk.PhotoImage(file = "./fotos/camera-re.jpg")
c11 = tk.Checkbutton(raiz, text = "Camera de re", variable = escolhaCamera_de_re,  width=100, height=100, compound='top', bg=background)
c11.grid(row = 8, column = 1, pady = 5)

#caixa de selecao do Direcao eletrica
# img12 = ImageTk.PhotoImage(file = "./fotos/direcao_eletrica.jpg")
c12 = tk.Checkbutton(raiz, text = "Direcao eletrica", variable = escolhaDirecao_eletrica,  width=100, height=100, compound='top', bg=background)
c12.grid(row = 9, column = 2, pady = 5)

#caixa de selecao do Vidros eletricos
# img13 = ImageTk.PhotoImage(file = "./fotos/vidro_eletrico.jpg")
c13 = tk.Checkbutton(raiz, text = "Vidros eletricos", variable = escolhaVidros_eletricos,  width=100, height=100, compound='top', bg=background)
c13.grid(row = 9, column = 0, pady = 5)

#caixa de selecao do Piloto automatico
# img14 = ImageTk.PhotoImage(file = "./fotos/piloto_automatico.jpg")
c14 = tk.Checkbutton(raiz, text = "Piloto automatico", variable = escolhaPiloto_automatico,  width=100, height=100, compound='top', bg=background)
c14.grid(row = 9, column = 1, pady = 5)
"""

#caixa Confirmar
b1 = tk.Button(raiz, text="Confirmar", command = detectarRecomendacao, bg=background)
b1.grid(row = 10, column = 0, padx = 10, pady=10)

#caixa Limpar areas selecionadas
b2 = tk.Button(raiz, text="Limpar areas selecionadas", command = limpar, bg=background)
b2.grid(row = 10, column = 2, padx = 5, pady=10 )

####    layout tela final: modelo do carro, disponibilidade de cores e preço final    ####

#resposta de qual carro foi recomendado
l2 = tk.Label(raiz, text = "Esse é seu carro:", bg=background)
l2.grid(row = 11, column = 0, pady = 2)
celularRecomendado = tk.Text(raiz, state = tk.DISABLED, height = 1, width=40)
celularRecomendado.grid(row = 11, column = 1, pady = 2)

#resposta do preço do carro
l4 = tk.Label(raiz, text="Preço do carro:", bg=background)
l4.grid(row = 13, column = 0, pady = 2)
precoCelular = tk.Text(raiz, state = tk.DISABLED, height = 1, width=40)
precoCelular.grid(row = 13, column = 1, pady = 2)

#loop da main para funcionamento do aplicativo
raiz.mainloop()