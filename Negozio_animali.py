#!/usr/bin/env python3

class Animale:

    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        self.sazio = False


    def __str__(self):
        return f"{self.nome} ({self.specie}) - {'Sazio' if self.sazio else 'affamato'}"



    def alimentato(self):
        self.sazio = True


    def vendere(self):
        self.alimentato = False


class NegozioAnimali:

    def __init__(self, nome):
        self.nome = nome
        self.animali = []

    def aggiungere_animale(self, animale):
        self.animali.append(animale)

    def mostrare_animali(self):
        for animale in self.animali:
            print(animale)


    def dato_cibo(self):
        for animale in self.animali:
            animale.alimentato()


    def vendere_animale(self, nome):
        for animale in self.animali:
            if animale.nome == nome:
                animale.vendere()
                self.animali.remove(animale)
                return

        print(f"Non c'e' nessun animale con nome {nome} nel negozio")



if __name__ == '__main__':

    negozio = NegozioAnimali("Il mondo a 4 zampe")

    gatto = Animale("Sofia", "Gatto")
    cane = Animale("Pinolo", "Cane")

    negozio.aggiungere_animale(gatto)
    negozio.aggiungere_animale(cane)

    negozio.mostrare_animali()
    negozio.dato_cibo()
    print(f"mostrando gli animali una volta che hanno mangiato")
    negozio.mostrare_animali()
    negozio.vendere_animale("Sofia")

    print(f"Mostrando gli animali in negozio")
    negozio.mostrare_animali()
