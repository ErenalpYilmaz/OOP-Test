## Ayni isimdeki methodlarin veya fonksiyonlarin farkli amaca hizmet edebilmesine polymorphism denir.

class Elma():
    def __init__(self,isim):
        self.isim = isim

    def bilgiVer(self):
        return self.isim + " 100 Kaloridir. "

class Muz():
    def __init__(self,isim):
        self.isim = isim

    def bilgiVer(self):
        return self.isim + " 150 kaloridir. "

elma = Elma("elma")
muz = Muz("muz")

meyveList = [elma,muz] #--> Nesneleri de listeye atabiliriz.

for meyve in meyveList:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(muz)