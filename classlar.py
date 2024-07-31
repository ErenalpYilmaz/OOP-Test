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

superman = SuperHero("Batman",39,"Gazeteci","Zengin")

print(superman.ornekmethod())