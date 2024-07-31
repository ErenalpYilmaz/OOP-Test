#Inheritence
class Hayvan():
    def __init__(self):
        print("Hayvan Sinifi init calisti")

    def method1(self):
        print("Hayvan Sinifi method1 ")

    def method2(self):
        print("Hayvan Sinifi method2 calisti")

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi Sinifi init cagirildi")

    def miyavla(self):
        print("miyavv")

    def method1(self): # override
        print("Kedi sinifindaki method1 cagirildi.")

myAnimal = Hayvan()
myCat = Kedi()
myCat.method1()
myCat.miyavla()
myCat.method1()

#kedi sinifindan hayvan sinifinin verilerini kullanabilir
#Eger iki classta da ayni method var ise nesneyi olusturdugunuz sinif hangisi ise ondakini kullanir.
#nesnede kedi classdaki  method1 i cagirdim onceden hayvan class indan geliyordu
