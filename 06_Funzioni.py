def saluto(nome):
    print(f"Ciao {nome}")
    
saluto("Giuseppe")    


def somma(x, y):
    return x + y

## risultato = somma(2, 8)
        
print(f"la somma tra questi due numeri e' {somma(10, 4)}")  

variabile = "Sono globale"
def mia_funzione():
      global variabile
      variabile = "Sono globale ma sono stata modificata"
      print(variabile)
      
mia_funzione()      
print(variabile)