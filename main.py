class coba:
    def __init__(self, nama):
        self.nama = nama
    
    def out(self):
        print(self.nama)

    def makeWith(self, name):
        print(self.nama + " with " + name)


namaku = coba("alvin")
namanya = coba("dvync")

namaku.out()
namanya.out()

namaku.makeWith(namanya.nama)
