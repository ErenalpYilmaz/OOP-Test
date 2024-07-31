#Ozel Methotlar

class Meyve():
    def __init__(self,isim,kalori):
        self.isim = isim
        self.kalori = kalori

    def __str__(self): #-->Yazdirilinca ne dondurucegini belirten methot
        return f"{self.isim} su kadar kaloriye sahiptir:{self.kalori}"

    def __len__(self):
        return self.kalori#-->

muz = Meyve("muz",150)
print(muz)
print(len(muz))

elma = Meyve("Elma",200)
print(len(elma))