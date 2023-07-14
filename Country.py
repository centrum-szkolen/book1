

class Country:

    def __init__(self,nazwa,populacja,stolica):
        self.nazwa = nazwa
        self.populacja = populacja
        self.stolica = stolica

    def information(self):
        print("Kraj: " + self.nazwa)
        print("Stolica: " + self.stolica)

    def compare(self,country_to_cmp):
        if self.populacja > country_to_cmp.populacja:
            print("Większą populacja ma: " + self.nazwa)
        elif self.populacja < country_to_cmp.populacja:
            print("Większą populacja ma: " + country_to_cmp.nazwa)
        else:
            print("Kraje mają takie same populacje.")

Polska = Country("Polska",300,"Warszawa")
Niemcy = Country("Niemcy",100,"Berlin")

Polska.information()

Polska.compare(Niemcy)