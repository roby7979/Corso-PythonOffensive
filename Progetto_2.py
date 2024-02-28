nome = input("Perfavore dimmi il tuo nome? ")
vendita = input("Dimmi il totale delle tue vendite del mese: ")

vendita = int(vendita)

commissione = vendita * 13 / 100

commissione = round(commissione)

print(f"Ciao {nome}, le tue commissioni per questo mese sono {commissione}")