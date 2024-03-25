class Persona:
    
    def __init__(self, nome, eta): # Persone. : __init__(roberto, nome, eta)
        self.nome = nome # roberto.nome = "Roberto"
        self.eta = eta # roberto.eta = 44
    

    def presentazione(self): #Persona.presentazione(roberto)
        print(f"Ciao sono {self.nome} e ho {self.eta} anni") # roberto.nome roberto.eta
    
roberto = Persona("Roberto", 44)    
roberto.presentazione()
    
    
    
    


class Calcolatrice:
    
    def __init__(self, num): # Calcolatrice. __init__(calc, numero)
        self.num = num # calc.num = 5
        
        
    def somma(self, altro_numero): # Calcolatrice.somma (calc, 8) 
        return self.num + altro_numero # calc.numero + 8 -> 5 + 8
        
        
    def doppia_somma(self, num1, num2): # Calcolatrice.doppia_somma(calc, 2, 9)   
        print(self.somma(num1) + self.somma(num2))
        
        
        
        
calc =  Calcolatrice(5)        
calc.somma(8)
calc.doppia_somma(2, 9)