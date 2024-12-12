class Car:

    def __init__(self,name,year,engine):
        self.name = name
        self.year = year
        self.engine = engine
    
    def running (self):
        print("Mobil sedang berjalan")
    
    def stop(self):
        print("Mobil sedang berhenti")

mobill = Car("toyota",2020,"V8")
mobill.running()
print(mobill.name)
mobil2 = Car("honda",1997,"V10")
print(mobil2.name)
mobil2.running()