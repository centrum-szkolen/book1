



class Language:

    def __init__(self,name,popularity,year):
        self.name = name
        self.popularity = popularity
        self.year = year
        # self.__secret()
    
    def show_details(self):
        print("Wybrałeś język " + self.name)

    def __secret(self):
        print("Sekretne informacje")




javascript = Language("Javascript",90,1993)
javascript.show_details()

javascript._Language__secret()

php = Language("PHP",70,1991)
php.show_details()


        
