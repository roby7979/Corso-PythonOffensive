class Persona:
    
    
    
    def __init__(self, nome, eta):
        
        self.nome = nome
        self.eta = eta
        
    def saluto(self):    
        return f"ciao sono {self.nome} e ho {self.eta} anni"
    
roberto = Persona("Roberto", 44)  
margherita = Persona("Margherita", 23)  
print(roberto.saluto())
print(margherita.saluto())




class Animale:
    
    def __init__(self, nome, genere):
        
        self.nome = nome
        self.genere = genere
        
    def descrizione(self):
        print (f"{self.nome} e' un {self.genere}")    
    
gatto = Animale("Pino", "gatto")   
cane = Animale("Pancho", "cane")    

print(gatto.descrizione())
print(cane.descrizione())




class ContoBancario:
    def __init__(self, conto, nome, soldi=0):
    
        self.conto = conto
        self.nome = nome
        self.soldi = soldi
        
        
    def depositare_soldi(self, soldi):
            self.soldi += soldi

            return f"\n [+] [{self.nome}] Hai depositato {soldi} euro, e attualmente hai in banca {self.soldi} euro"
        
    def ritiro_soldi(self, soldi):  
          if soldi > self.soldi:
              return f"\n [!] [{self.nome}] Operazione Negata, fondi insufficieti"
              
          self.soldi -= soldi    
          
          return f"\n [+] [{self.nome}] Hai ritirato {soldi} euro, e attualmente hai in banca {self.soldi} euro"
    
Marco = ContoBancario("16253627", "Marco Bianchi", 1000)    
Chiara = ContoBancario("3312232", "Chiara rossi", 20)

print(Marco.depositare_soldi(500))
print(Marco.ritiro_soldi(900))
print(Marco.ritiro_soldi(1800))

print(Chiara.ritiro_soldi(10))




class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
      
    @property    
    def area(self):
        
        return self.base * self.altezza    
        
    def __str__(self):
        return f" le proprieta' del rettangolo: Base:{self.base} Altezza:{self.altezza}" 
        
    def __eq__(self, altro):    
        return self.base == altro.base and self.altezza == altro.altezza
        
ret1 = Rettangolo(20, 80)   
ret2 = Rettangolo(20, 80)     
print(f"\n [+] l'area e' {ret1.area}")
print(ret1)
print(f"sono uguali? -> {ret1 == ret2}")




class Libro:
    
    IVA = 0.21
    
    def __init__(self, titolo, autore, prezzo):
        
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
    
    @staticmethod #Decoratore
    def e_bestseller(totale_vendite):
        return totale_vendite > 5000
    
    
    @classmethod #Decoratore
    def prezzo_con_iva(cls, prezzo):
     
     return prezzo + prezzo * cls.IVA
    
mio_libro = Libro("Come imparare l'hacking", "Roby7979", 17.5)   
print(f" Il prezzo del libro con IVA e' di {Libro.prezzo_con_iva(mio_libro.prezzo)}")











