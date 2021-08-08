from experta import Rule, Fact, KnowledgeEngine, AND

#classe de regras para a recomendacao do celular
class RegrasRecomendacao(KnowledgeEngine):
    #variaveis para as respostas
    celular = ""
    precodoCelular = ""

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='2'), Fact(tipoMultiChip='sim')))
    def escolhaMotorolaMotoE6i(self):
        self.celular = "Motorola Moto E6i"
        self.precodoCelular = "R$ 699,00"

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camFrontal='sim'), Fact(marca='lg')))
    def escolhaLGK62(self):
        self.celular = "LG K62"
        self.precodoCelular = "R$ 1.049,00"

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='4'), Fact(capacidade='128'), Fact(camFrontal='20')))
    def escolhaMotorolaOneAction(self):
        self.celular = "Motorola One Action"
        self.precodoCelular = "R$ 1.149,00"
    
    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='6')))
    def escolhaMi9T(self):
        self.celular = "Mi 9T"
        self.precodoCelular = "R$ 1.340,00"    

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camFrontal='13'), Fact(marca='samsung')))
    def escolhaSamsungGalaxyA21s(self):
        self.celular = "Samsung Galaxy A21s"
        self.precodoCelular = "R$ 1.435,00"

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='4'), Fact(capacidade='128'), Fact(camFrontal='13')))
    def escolhaSamsungGalaxyA31(self):
        self.celular = "Samsung Galaxy A31"
        self.precodoCelular = "R$ 1.619,00"

    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='2'), Fact(tipoMultiChip='nao')))
    def escolhaIPhone6(self):
        self.celular = "iPhone 6S"
        self.precodoCelular = "R$ 1.749,00"
    
    @Rule(AND(Fact(tipoPreco='2000'), Fact(tipoRam='4'), Fact(capacidade='64'), Fact(camPrincipal='12')))
    def escolhaZenFone5(self):
        self.celular = "ZenFone 5"
        self.precodoCelular = "R$ 1.799,00"
    
    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='6'), Fact(capacidade='128'), Fact(marca='lg')))
    def escolhaLGVelvet(self):
        self.celular = "LG Velvet"
        self.precodoCelular = "R$ 2.299,00"

    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='6'), Fact(capacidade='128'), Fact(marca='xiaomi')))
    def escolhaPocoF3(self):
        self.celular = "Poco F3"
        self.precodoCelular = "R$ 2.679,00"
    
    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='12')))
    def escolhaMotorolaMotoG100(self):
        self.celular = "Motorola Moto G100"
        self.precodoCelular = "R$ 2.852,00"

    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='3')))
    def escolhaIPhoneX(self):
        self.celular = "iPhone X"
        self.precodoCelular = "R$ 3.799,00"
    
    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='6'), Fact(capacidade='64')))
    def escolhaZenFone6(self):
        self.celular = "ZenFone 6"
        self.precodoCelular = "R$ 3.799,00"
    
    @Rule(AND(Fact(tipoPreco='2a5'), Fact(tipoRam='8')))
    def escolhaSamsungGalaxyS21(self):
        self.celular = "‎Samsung Galaxy S21"
        self.precodoCelular = "R$ 3.869,00"

    @Rule(AND(Fact(tipoPreco='5000'), Fact(tipoRam='8'), Fact(camFrontal='64')))
    def escolhaZenFone7Pro(self):
        self.camcelular = "ZenFone 7 Pro"
        self.precodoCelular = "R$ 6.497,00"
    
    @Rule(AND(Fact(tipoPreco='5000'), Fact(tipoRam='8'), Fact(camPrincipal='20')))
    def escolhaMi11(self):
        self.celular = "Mi 11"
        self.precodoCelular = "R$ 7.189,00"

    @Rule(AND(Fact(tipoPreco='5000'), Fact(tipoRam='6')))
    def escolhaIPhone12(self):
        self.celular = "iPhone 12"
        self.precodoCelular = "R$ 7.199,00"
