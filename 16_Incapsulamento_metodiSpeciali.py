class Esempio:
    
    def __init__(self):
        
        #Attributo Protetto
        self._attributo_protetto = "sono un attributo protetto, e non dovresti vedermi"
        
        
esempio = Esempio()
print(esempio._attributo_protetto)        


class Esempio1:
    
    def __init__(self):
        
        #Attributo Privato
        self.__attributo_privato = "sono un attributo privato, e non dovresti vedermi" # name mangling 
        
        
esempio1 = Esempio1()
print(esempio1._Esempio1__attributo_privato) 












class Automobile:
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.__chilometraggio = 0 #attributo privato
    
    
    def guidare(self, chilometri):
        
        if chilometri >= 0:
            self.__chilometraggio += chilometri
        else:
            print("I chilometri devono essere maggiori di 0")
            
            
    def mostrare_chilometri(self):      
        return self.__chilometraggio
    
auto = Automobile("BMW", "330")    
auto.guidare(150)
print(auto._Automobile__chilometraggio)







class Libro:
    
    def __init__(self, autore, titolo):
        
        self.autore = autore
        self.titolo = titolo 
    
    
    def __str__(self):
        
        return f"il libro {self.titolo} e' stato scritto da {self.autore}"
    
    
    def __eq__(self, altro):
        
        return self.autore == altro.autore and self.titolo == altro.titolo
        
    
    
libro = Libro("Roby7979", "Tutorial Hacking")    
libro_2 = Libro("Roby7979", "Tutorial Hacking numero 6")
print(libro)
print(f"questi libri sono uguali? {libro == libro_2}")






class ContoBancario:
    
    def __init__(self, num_conto, titolare, saldo_iniziale=0):
        
        self.num_conto = num_conto
        self.titolare = titolare
        self.__saldo = saldo_iniziale #attributo privato
        
        
    def depositare_soldi(self, quantita):
        
        if quantita > 0:
            self.__saldo += quantita
            print(f"Saldo attuale nel conto {self.__saldo}")
        else:
            print("la quantita e' ioncorretta")
        
        
    def ritirare_soldi(self, quantita):
        
        if quantita > 0:
            if quantita > self.__saldo:
                print(f"la quantita che vuoi ritirare e' maggiore del tuo saldo")
            else:
                self.__saldo -= quantita  
                print(f"Saldo attuale nel conto {self.__saldo}")   
        else:
            print("la quantita non e' corretta")    
        
        
    def mostrare_soldi(self):   
        
        return f"Il saldo attuale e' {self.__saldo}"         
        
        
mario = ContoBancario("1657261", "Mario Rossi", 1500)  
mario.depositare_soldi(500)      
mario.ritirare_soldi(200)

print(mario.mostrare_soldi())




class Cassa:
    
    def __init__(self, *items):
        
        self.items = items
        
        
    def __len__(self):
        
        return len(self.items)    
   
            
cassa = Cassa("Mela", "Banana", "Kiwi", "Mandarino", "Pesca")
print(len(cassa))               


















































