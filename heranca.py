class veiculo:
    def __init__(self, nome):
        self.nome = nome
    def dirigir (self):
        print("Está dirigindo: ", self.nome)

class voador:
    def __init__(self, nome):
        self.nome = nome
    def voar (self):
        print("Está voando: ", self.nome)

class flutuante:
    def __init__(self, nome):
        self.nome = nome
    def flutuar (self):
        print("Está flutuando: ", self.nome)

class veículo_Anfíbio (veiculo, voador, flutuante):
    def __init__(self, n):
        veiculo.__init__(self, n)
        voador.__init__(self, n)
        flutuante.__init__(self, n)

carro_Anfibio = veículo_Anfíbio ("Carro Anfíbio")
carro_Anfibio.dirigir()
carro_Anfibio.voar()
carro_Anfibio.flutuar()