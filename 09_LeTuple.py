esempio = (1, "test", [1, 2, 3], 4, True, {'mela':1, 'pere':2}, 5) # immutabile insert(), extend(), remove(), append()
#esempio = [1, "test", (1, 2, 3), 4, True, {'mela':1, 'pere':2}, 5] # mutabile
#print(type(esempio))

#print(esempio[3:])

#print(esempio)

#for elementi in esempio:
    #print(elementi)
    
    
#esempio2 = (5, 6, 7, 8, 9)

#esempio3 = esempio*3
 
#print(esempio3)

mia_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9,)

numeri_pari = tuple(pino for pino in mia_tupla if pino % 2 == 1)

print(numeri_pari)


db1_credenziali = ("roby", "roby123")
db2_credenziali = ("franco", "franco456")

try:
    db1_credenziali[0] = "giuseppe"

except TypeError:
    print("Non e' possibile manipolare gli elementi di una tupla")

