# LISTE

my_ports = [22, 80, 443, 8080, 445, 443, 22]

my_ports.extend([84, 85])

my_ports += [86, 87]

my_ports = sorted(my_ports)

del my_ports[0]

for port in my_ports:
    print(f"Porta: {port}")
    
print(f"\n[+]La lista ha un totale di {len(my_ports)} elementi")

mia_lista = [1, 2, 3, 4, 5]
print(mia_lista[-2])

mia_lista.insert(2, "Ciao")
print(mia_lista)

print(mia_lista.pop())

print(mia_lista)

print(mia_lista.pop())

print(mia_lista)


mia_lista2 = [2, 45, 22, 11, 18, 90, 78, 25, 2]
print(mia_lista2)

print(mia_lista2.index(90))

print(mia_lista2[5])

mia_lista2 += [45, 90]
print(mia_lista2)

print(mia_lista2.index(90))

for x, y in enumerate(mia_lista2):
    print(f"{x}: {y}")
    
mia_lista2 = sorted(mia_lista2)   
print(mia_lista2)
mia_lista2 = set(mia_lista2)
print(mia_lista2)

print(f"Il numero piu alto nella lista e {max(mia_lista2)}")
print(f"Il numero piu basso nella lista e {min(mia_lista2)}")

somma = sum(mia_lista2)
print(somma)


