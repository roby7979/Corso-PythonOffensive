testo = input("Inserisci un testo a tua scelta: ")
lettere = []

testo = testo.lower()

lettere.append(input("Inserisci la tua prima lettera: ".lower()))
lettere.append(input("Inserisci la tua seconda lettera: ".lower()))
lettere.append(input("Inserisci la tua terza lettera: ".lower()))

print("\n")
print("QUANTITA' LETTERE")
quantita_lettere1 = testo.count(lettere[0])
quantita_lettere2 = testo.count(lettere[1])
quantita_lettere3 = testo.count(lettere[2])

print(f"Abbiamo trovato la lettera '{lettere[0]}' ripetuta {quantita_lettere1} volte")
print(f"Abbiamo trovato la lettera '{lettere[1]}' ripetuta {quantita_lettere2} volte")
print(f"Abbiamo trovato la lettera '{lettere[2]}' ripetuta {quantita_lettere3} volte")

print("\n")
print("QUANTITA' DI PAROLE")
parole = testo.split()
print(f"Abbiamo trovato {len(parole)} parole nel tuo testo")

print("\n")
print("LETTERA DI INIZIO E FINE")
lettera_inizio = testo[0]
lettera_fine = testo[-1]
print(f"La letra inicial es '{lettera_inizio}' y la letra final es '{lettera_fine}'")

print("\n")
print("TESTO INVERTITO")
parole.reverse()
testo_invertito = ' '.join(parole)
print(f"Se ordiniamo il tuo testo al rovescio dice: '{testo_invertito}'")

print("\n")
print("CERCANDO LA PAROLA PYTHON")
cerca_python = 'python' in testo
dic = {True:"sí", False:"no"}
print(f"La parola 'Python' {dic[cerca_python]} e' stata trovata nel testo")