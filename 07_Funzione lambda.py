mia_funzione = lambda: "Ciao a tutti"
print(mia_funzione())

quadrato = lambda numero: numero ** 2  
print(quadrato(8))

somma = lambda x, y: x + y
print(somma(10, 8))

numeri = [1, 2, 3, 4, 5]
quadrato1 = list(map(lambda x: x**2, numeri))
print(quadrato1)


numeri1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pari = list(filter(lambda x: x % 2 != 0, numeri1))
print(pari)
