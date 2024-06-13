# Class mobil 
class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0
        
    def tambah_kecepatan(self, increment):
        self.kecepatan += increment
        
    def kurangi_kecepatan(self, decrement):
        self.kecepatan -= decrement
    
    def info(self):
        return f"Mobil bermerek= {self.merek}, \n model= {self.model} \n tahun= {self.tahun}"
    

# Object Class Mobil 
sedan = Mobil("BMW", "M3", 2000)
jeep = Mobil("Suzuki", "Jimny", 1990)

print(sedan.info)
print(jeep.info) 
    
    