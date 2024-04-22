
import time 
def mio_decoratore(funzione): #Funzione di Ordine superiore
    def involucro():
        print("Sto salutando dentro il decoratore, prima di chiamare la funzione")
        funzione()
        print("Sto salutando dentro il decoratore, dopo aver chiamato la funzione")

    return involucro



@mio_decoratore
def Saluto():
    
    print("Ciao sto salutando da dentro la funzione")
    
Saluto()    






class Persona:
    
    def __init__(self, nome, eta):
        self._nome = nome
        self._eta = eta
        
    @property     
    def eta(self): # Getter
        return self._eta
    
    @eta.setter # Setter
    def eta(self, valore):
        if valore > 0:
            self._eta = valore
        else:
            raise ValueError("La eta non puo essere un numero negativo")
     
mario = Persona("Mario", 30)  
mario.eta = 14 # Setter
print(mario.eta) # Getter






import time 

def cronometro(funzione):
    def Involucro():
        inizio = time.time()
        funzione()
        fine = time.time()
        
        print(f"Tempo totale trascorso {funzione.__name__}: {fine - inizio}")
    return Involucro    

@cronometro
def pausa_corta():
    time.sleep(1)
    
@cronometro
def pausa_lunga():
    time.sleep(2)

pausa_corta()
pausa_lunga()



#*args

#def somma(*args):
    
    
#print(somma(2, 3, 4, 90, 33))    


#*Kwargs

def presentazione(**kwargs):
    
    print(type(kwargs))
    
    
presentazione(nome="Roby", eta=44, citta="Barcellona")
















































