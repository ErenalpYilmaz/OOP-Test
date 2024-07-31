####               classlar               ####
## instance --> nesne && attribute --> Sinif ozellikleri ##

class SuperHero():

    def __init__(self,isim,yas,meslek,ozelguc):
        print("Init cagirildi")
        self.isim = isim
        self.yas = yas
        self.meslek= meslek
        self.ozelguc = ozelguc

    def ornekmethod(self):
        print(f"I am superhero and my Job is :{self.meslek}")


## Default Degerler ##
#Kopek 1 yas --> insan 7 yas
class Kopek():
    yilCarpani = 7

    def __init__(self,yas=0): #--> Bos deger verildiginde hata vermesini istemiyorsan default deger ver.
        self.yas = yas

    def insanYasi(self):
        return self.yas * self.yilCarpani

myDog = Kopek(3)
print(myDog.yas)
print(f"Insan yasi = {myDog.insanYasi()}")