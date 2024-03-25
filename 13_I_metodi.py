class Calcolatrice:
    
    @staticmethod
    def somma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def divisione(num1, num2):
        return num1 / num2 if num2 != 0 else "ERROR: non si puo' dividere un numero per zero"
    
    @staticmethod
    def moltiplicazione(num1, num2):
        return num1 * num2
    
        
    @staticmethod
    def sottrazione(num1 ,num2):
        return num1 - num2   
        
    
print(Calcolatrice.somma(2, 8))
print(Calcolatrice.divisione(8, 0))
print(Calcolatrice.moltiplicazione(5, 10))
print(Calcolatrice.sottrazione(10, 7))




class Automobile:
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    @classmethod
    def sportivi(cls, marca):
        return cls(marca, "Sportivo")
    
    
    @classmethod
    def normale(cls, marca):
        return cls(marca, "normale")
        
    
    
    def __str__(self):
        return f"La marca {self.marca} e' un modello {self.modello}"
         
         
sportivo = print(Automobile.sportivi("Ferrari"))            
# Automobile("Ferrari", "Sportivo")
normale = print(Automobile.normale("Fiat")) 







class Studente:
    
    studente = []
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
        Studente.studente.append(self)
        
    
    @staticmethod
    def maggiorenne_di_eta(eta):
        return eta >= 18
    
    @classmethod
    def creare_studente(cls, nome, eta):
        if cls.maggiorenne_di_eta(eta):
            return cls(nome, eta)
        else:
            print(f"Errore: Lo studente {nome} e' minore di eta")
            
    @staticmethod
    def mostrare_studente():        
        for i, studente in enumerate(Studente.studente):
            print(f"\tStudente numero {i+1}: {studente.nome}")

Studente.creare_studente("roby7979", 44)
Studente.creare_studente("Super_x", 17)
Studente.creare_studente("Killberg", 40)
Studente.creare_studente("Manolo", 8)

print("Lista dei studenti esistenti")

Studente.mostrare_studente()



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        







