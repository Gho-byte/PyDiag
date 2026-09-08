from abc import abstractmethod, ABC

class Modele(ABC):
    def __init__(self):
        raise TypeError("You Can't Create Insance From This Class")

    @abstractmethod
    def entrainer(data):
        pass

    @abstractmethod
    def predicte(input):
        pass

class ModeleMoyenne(Modele):
    def __init__(self):
        self.weight = 0

    def predicte(self, input, data):
        self.entrainer(data)
        print(f'[+] Moyenne Model Prediction: {input * self.weight + 1}')
    
    def entrainer(self, data):
        self.weight = sum(data)

class ModeleLineaireSimple(Modele):
    def __init__(self, weight, bias=1):
        self.weight = weight
        self.bias = bias

    def predicte(self, input, data):
        self.entrainer(data)
        print(f'[+] Linear Model Prediction: {input * self.weight + self.bias}')

    def entrainer(self, data):
        self.weight -= 0.000365

class Pipeline:
    def __init__(self, pretraitement, modele):
        self.data = pretraitement
        self.model = modele

    def executer(self, data, input):
        prediction = self.model.predicte(input, data)

def normaliser(donnees):
    maximum = max(donnees)
    return [d / maximum for d in donnees]


donnees = [5, 8, 11]
normaliser = normaliser(donnees)

pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=ModeleLineaireSimple(2, 1))

for pipeline in [pipeline_moyenne, pipeline_lineaire]:
    resultat = pipeline.executer(data=donnees, input=5)
    print(type(pipeline.model).__name__, "->", resultat)