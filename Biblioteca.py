#!/usr/bin/env python3

class Libro:

    def __init__(self, id_libro, autore, nome_libro):
        self.id_libro = id_libro
        self.autore = autore
        self.nome_libro = nome_libro
        self.prestato = False

    def __str__(self):
        return f"Libro ({self.id_libro}, {self.autore}, {self.nome_libro})"

    def __repr__(self):
        return self.__str__()


class Biblioteca:

    def __init__(self):
        self.libri = {} # {1: Libro(1, "roby7979", "come imparare hacking")}

    def aggiungere_libro(self, libro):
        if libro.id_libro not in self.libri:
            self.libri[libro.id_libro] = libro

        else:
            print(f"Non e' possibile aggiungere il libro con ID {libro.id_libro}")


    def prestare_libro(self, id_libro):
         if id_libro in self.libri and not self.libri[id_libro].prestato:
                self.libri[id_libro].prestato = True
         else:
            print(f"Non e' possibile prestare il libro con ID {id_libro}")


    @property
    def mostrare_libri(self):
        return [libro for libro in self.libri.values() if not libro.prestato]

    @property
    def mostrare_libri_prestati(self):
        return [libro for libro in self.libri.values() if libro.prestato]


class BibliotecaInfantile(Biblioteca):

    def __init__(self):
        super().__init__()
        self.libri_per_bambini = {} # -> {1: True, 2: False}

    def aggiungere_libro(self, libro, per_bambini):
        super().aggiungere_libro(libro)
        self.libri_per_bambini[libro.id_libro] = per_bambini

    def prestare_libro(self, id_libro, bambini):
        if id_libro in self.libri and self.libri_per_bambini[id_libro] == bambini and not self.libri[id_libro].prestato:
            self.libri[id_libro].prestato = True
        else:
            print(f"Non e' possibile prerstare libro conm ID {id_libro}")

if __name__ == '__main__':

    biblioteca = BibliotecaInfantile()

    libro1 = Libro(1, "Roby7979", "Come imparare l hacking")
    libro2 = Libro(2, "Franco", "Impara a colorare")

    biblioteca.aggiungere_libro(libro1, per_bambini = False)
    biblioteca.aggiungere_libro(libro2, per_bambini = True)

    print(f"Libri presenti nella Biblioteca {biblioteca.mostrare_libri}")


    biblioteca.prestare_libro(1, bambini=False)
    print(f"Libri presenti nella Biblioteca {biblioteca.mostrare_libri}")
    print(f"Libri prestati {biblioteca.mostrare_libri_prestati}")