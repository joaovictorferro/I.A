from experta import Rule, Fact, KnowledgeEngine, AND, fact

#classe de regras para a recomendacao do celular
class RegrasRecomendacao(KnowledgeEngine):
    #variaveis para as respostas
    celular = ""
    precodoCelular = ""
    imagem = ""

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='2'), Fact(tipoMultiChip='2')))
    def escolhaMotorolaMotoE6i(self):
        self.celular = "Motorola Moto E6i"
        self.precodoCelular = "R$ 699,00"
        self.imagem = r".\Fotos\MotorolaMotoE6i.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camFrontal='1'), Fact(marca='2')))
    def escolhaLGK62(self):
        self.celular = "LG K62"
        self.precodoCelular = "R$ 1.049,00"
        self.imagem = r".\Fotos\LGK62.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='4'), Fact(capacidade='128'), Fact(marca='4')))
    def escolhaMotorolaOneAction(self):
        self.celular = "Motorola One Action"
        self.precodoCelular = "R$ 1.149,00"
        self.imagem = r".\Fotos\MotorolaOneAction.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='6')))
    def escolhaMi9T(self):
        self.celular = "Mi 9T"
        self.precodoCelular = "R$ 1.340,00"    
        self.imagem = r".\Fotos\Mi9T.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camFrontal='1'), Fact(marca='5')))
    def escolhaSamsungGalaxyA21s(self):
        self.celular = "Samsung Galaxy A21s"
        self.precodoCelular = "R$ 1.435,00"
        self.imagem = r".\Fotos\SamsungGalaxyA21s.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='4'), Fact(capacidade='128'), Fact(marca='5')))
    def escolhaSamsungGalaxyA31(self):
        self.celular = "Samsung Galaxy A31"
        self.precodoCelular = "R$ 1.619,00"
        self.imagem = r".\Fotos\SamsungGalaxyA31.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='2'), Fact(tipoMultiChip='1')))
    def escolhaIPhone6(self):
        self.celular = "iPhone 6S"
        self.precodoCelular = "R$ 1.749,00"
        self.imagem = r".\Fotos\iPhone6s.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='2'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camPrincipal='2')))
    def escolhaZenFone5(self):
        self.celular = "ZenFone 5"
        self.precodoCelular = "R$ 1.799,00"
        self.imagem = r".\Fotos\ZenFone5.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='6'), Fact(capacidade='128'), Fact(marca='2')))
    def escolhaLGVelvet(self):
        self.celular = "LG Velvet"
        self.precodoCelular = "R$ 2.299,00"
        self.imagem = r".\Fotos\LGVelvet.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='6'), Fact(capacidade='128'), Fact(marca='6')))
    def escolhaPocoF3(self):
        self.celular = "Poco F3"
        self.precodoCelular = "R$ 2.679,00"
        self.imagem = r".\Fotos\PocoF3.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='12')))
    def escolhaMotorolaMotoG100(self):
        self.celular = "Motorola Moto G100"
        self.precodoCelular = "R$ 2.852,00"
        self.imagem = r".\Fotos\MotorolaMotoG100.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='3')))
    def escolhaIPhoneX(self):
        self.celular = "iPhone X"
        self.precodoCelular = "R$ 3.799,00"
        self.imagem = r".\Fotos\iPhoneX.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='6'), Fact(capacidade='64')))
    def escolhaZenFone6(self):
        self.celular = "ZenFone 6"
        self.precodoCelular = "R$ 3.799,00"
        self.imagem = r".\Fotos\ZenFone6.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='25'), Fact(tipoRam='8')))
    def escolhaSamsungGalaxyS21(self):
        self.celular = "‎Samsung Galaxy S21"
        self.precodoCelular = "R$ 3.869,00"
        self.imagem = r".\Fotos\‎SamsungGalaxyS21.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='5'), Fact(tipoRam='8'), Fact(camFrontal='1')))
    def escolhaZenFone7Pro(self):
        self.celular = "ZenFone 7 Pro"
        self.precodoCelular = "R$ 6.497,00"
        self.imagem = r".\Fotos\ZenFone7Pro.jpg"
    
    # OK
    @Rule(AND(Fact(tipoPreco='5'), Fact(tipoRam='8'), Fact(camPrincipal='2')))
    def escolhaMi11(self):
        self.celular = "Mi 11"
        self.precodoCelular = "R$ 7.189,00"
        self.imagem = r".\Fotos\Mi11.jpg"

    # OK
    @Rule(AND(Fact(tipoPreco='5'), Fact(tipoRam='6')))
    def escolhaIPhone12(self):
        self.celular = "iPhone 12"
        self.precodoCelular = "R$ 7.199,00"
        self.imagem = r".\Fotos\iPhone12.jpg"
    
    #OK
    @Rule(AND(Fact(tipoRam='2'),Fact(marca='4')))
    def escolhaMotorolaMotoE6i(self):
        self.celular = "Motorola Moto E6i"
        self.precodoCelular = "R$ 699,00"
        self.imagem = r".\Fotos\MotorolaMotoE6i.jpg"

    # OK
    @Rule(AND(Fact(tipoRam='2'), Fact(marca='1')))
    def escolhaIPhone6(self):
        self.celular = "iPhone 6S"
        self.precodoCelular = "R$ 1.749,00"
        self.imagem = r".\Fotos\iPhone6s.jpg"
    
    # OK
    @Rule(AND(Fact(marca='3'),Fact(tipoRam='8')))
    def escolhaZenFone7Pro(self):
        self.celular = "ZenFone 7 Pro"
        self.precodoCelular = "R$ 6.497,00"
        self.imagem = r".\Fotos\ZenFone7Pro.jpg"
    
    # OK
    @Rule(AND(Fact(marca='5'), Fact(tipoRam='8')))
    def escolhaSamsungGalaxyS21(self):
        self.celular = "‎Samsung Galaxy S21"
        self.precodoCelular = "R$ 3.869,00"
        self.imagem = r".\Fotos\‎SamsungGalaxyS21.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='8'),Fact(marca='6')))
    def escolhaMi11(self):
        self.celular = "Mi 11"
        self.precodoCelular = "R$ 7.189,00"
        self.imagem = r".\Fotos\Mi11.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='4'), Fact(capacidade='128'), Fact(marca='4')))
    def escolhaMotorolaOneAction(self):
        self.celular = "Motorola One Action"
        self.precodoCelular = "R$ 1.149,00"
        self.imagem = r".\Fotos\MotorolaOneAction.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='4'), Fact(capacidade='128'), Fact(marca='5')))
    def escolhaSamsungGalaxyA31(self):
        self.celular = "Samsung Galaxy A31"
        self.precodoCelular = "R$ 1.619,00"
        self.imagem = r".\Fotos\SamsungGalaxyA31.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='4'), Fact(capacidade='64'), Fact(marca='3')))
    def escolhaZenFone5(self):
        self.celular = "ZenFone 5"
        self.precodoCelular = "R$ 1.799,00"
        self.imagem = r".\Fotos\ZenFone5.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='4'), Fact(capacidade='64'),Fact(marca='5')))
    def escolhaSamsungGalaxyA21s(self):
        self.celular = "Samsung Galaxy A21s"
        self.precodoCelular = "R$ 1.435,00"
        self.imagem = r".\Fotos\SamsungGalaxyA21s.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='4'), Fact(capacidade='64'),Fact(marca='2')))
    def escolhaLGK62(self):
        self.celular = "LG K62"
        self.precodoCelular = "R$ 1.049,00"
        self.imagem = r".\Fotos\LGK62.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='6'),Fact(marca='2')))
    def escolhaLGVelvet(self):
        self.celular = "LG Velvet"
        self.precodoCelular = "R$ 2.299,00"
        self.imagem = r".\Fotos\LGVelvet.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='6'),Fact(marca="1")))
    def escolhaIPhone12(self):
        self.celular = "iPhone 12"
        self.precodoCelular = "R$ 7.199,00"
        self.imagem = r".\Fotos\iPhone12.jpg"
    
    # OK
    @Rule(AND(Fact(tipoRam='6'), Fact(marca='3')))
    def escolhaZenFone6(self):
        self.celular = "ZenFone 6"
        self.precodoCelular = "R$ 3.799,00"
        self.imagem = r".\Fotos\ZenFone6.jpg"

    # OK
    @Rule(AND(Fact(tipoRam='6'),Fact(marca='6')))
    def escolhaPocoF3(self):
        self.celular = "Poco F3"
        self.precodoCelular = "R$ 2.679,00"
        self.imagem = r".\Fotos\PocoF3.jpg"
    