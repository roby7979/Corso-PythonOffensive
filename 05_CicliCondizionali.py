
names = ["Roberto", "Franco", "Pamela", "Giorgio"]


for name in names:
   print(f"Il nome per questo giro e' {name}")
    
    
i = 0
while i < 5:
    print(i)
    
    i += 1
    
    
names2 = ["Killberg", "Super_x", "Roby7979"]

for contatore, name in enumerate(names2):
    print(f"Nome [{contatore+1}]: {name}")    
    
    
frutta = {"mela": 2, "Banane": 1, "Mandarini": 5}   

for frutto, quantita in frutta.items():
    print(f"Ci sono {quantita} quantita della frutta {frutto}")
    
    
    
    
    
my_list = [[1, 4 ,5], [4, 7, 9], [8, 2, 1]] 

for elements in my_list:
    print(f"\n[+]Andiamo a elencare la lista {elements}\n")
    for element_in_list in elements:
        print(element_in_list)   
        
        
        
for i in range(10):
    
    if i == 5:
        print(f"Attualmente i e' 5 [{i}]")
    else:
        print(f"Attualmente i NON e' 5 [{i}]")
    
    
i = 0

while i < 16:
    if i == 10:
        print("Usciamo prima del tempo")
        break
    i += 1
else:
    print("Il ciclo si e' concluso correttamente")      
    
print("Stiamo fuori dal ciclo")      





eta = 12

if eta < 13:
    print("Sei un bambino")

elif  13 <= eta < 18:
      print("sei un adoloscente")
else:    
    print("Sei un adulto")
    
    
    
eta1 = 13
nazionalita = "Italiana"

if eta1 >= 18 or nazionalita != "Spagnola":
    print("Ok puoi votare")
else:
    print("Non sei spagnolo!")
    
    
    
lista2 = [1, 4, 12, 18, 44, 98]

if 55 in lista2:
    print("Questo numero e' presente")
else:
    print("Questo numero NON e' presente")        




          