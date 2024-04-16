class Animale:
    def __init__(self, nome):
        self.nome = nome   
    
    def parlare(self):
        pass 
      
class Gatto(Animale):  
    
    def parlare(self):
        return f"Miaooooooo"
    
    
class Cane(Animale):
    
    def parlare(self):
        return f"Bauuuuuu"    
      
def fa_parlare(oggetto):
    print(f"{oggetto.nome} dice {oggetto.parlare()}")
    
      
gatto = Gatto("Pino")
cane = Cane("Sofia")

fa_parlare(gatto)
fa_parlare(cane)





class Automobile:
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def descrizione(self):
        return f"Veicolo: {self.marca} {self.modello}"
    
    
class Macchina(Automobile):   
    
    def descrizione(self):
        return f"Macchine: {self.marca} {self.modello}"
    
    
class Moto(Automobile):
    
    def descrizione(self):
        return f"Moto: {self.marca} {self.modello}"
    
    
    
def descrizione_veicolo(veicolo): #Polimorfismo
        
    print(veicolo.descrizione())
           
macchina = Macchina("BMW", "M4")
moto = Moto("Honda", "cbr900")    

descrizione_veicolo(macchina)
descrizione_veicolo(moto)




class Dispositivo:
    
    def __init__(self, modello):
        self.modello = modello
        
    def scannerizzare_vulnerabilita(self):
        raise NotImplementedError("Questo metodo deve essere definito per il resto delle subclassi esistenti")
    
class Pc(Dispositivo):
    
    def scannerizzare_vulnerabilita(self):
        
        return f"Analisi delle vulnerabilita conclusa: Effettuare un aggiornamento del sistema, molti software non aggiornati"
    
    
    
class Router(Dispositivo):
    
    def scannerizzare_vulnerabilita(self):
        return f"Analisi delle vulnerabilita conclusa: Multiple porte aperte, si raccomanda chiudere le porte aperte"
    
    
    
    
class TelefonoCellulare(Dispositivo):
    
    def scannerizzare_vulnerabilita(self):
        return f"Analisi delle vulnerabilita conclusa: Multiple applicazioni con permessi eccessivi"



 
def realizzare_scan(dispositivo): # Polimorfismo
    print(dispositivo.scannerizzare_vulnerabilita())
    
pc = Pc("Lenovo")
router = Router("Tp-Link Archer C50")
cellulare = TelefonoCellulare("Samsung S23")     

realizzare_scan(pc)   
realizzare_scan(router)   
realizzare_scan(cellulare)


























