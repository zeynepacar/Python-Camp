#classes

class Banka:
    def kredi_basvur(self):
        print("Kredi başvurusu yapıldı.")
    
    def kredi_hesapla(self):
        print("Hesaplar yapıldı.")

# self = this (java)

banka = Banka()
banka.kredi_basvur()

class Matematik:
    # constructor bloğu
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladı. (referansı oluştus)")

    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
matematik = Matematik(6,7)
print(matematik.topla())
print(matematik.carp())

# inheritance
class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    
    def varyans_hesapla(self):
        return self.s1 * self.s2

istatistik = Istatistik(5,8)
print(istatistik.bol())

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


musteri = Person("Zeynep", "Acar")
print(musteri.name)