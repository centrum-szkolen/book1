class Country:
    def __init__(self,name, population,capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show_info(self):
        print("Kraj: " + self.name + " . Jego stolica to: " + self.capital)

    def compare_population(self, second_country):
        if self.population > second_country.population:
            print(self.name)
        elif self.population < second_country.population:
            print(second_country.name)
                


polska = Country("Poland", 200, "Warszawa")
niemcy = Country("Niemcy", 300, "Berlin")

polska.show_info()
polska.compare_population(niemcy)
