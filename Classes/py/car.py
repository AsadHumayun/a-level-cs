from types import NoneType


class Car:
    def __init__(self, name: str, miles: float, makemodel: str, clr: str, plate: str, insurcomp: str = "uninsured") -> NoneType:
        self.name = name
        self.mileage = miles
        self.make = makemodel.split(";")[0]
        self.model = makemodel.split(";")[1]
        self.clr = str(clr).capitalize()
        self.plate = plate
        self.insurance_company = insurcomp

    def compile(self):
        return self.__dict__.values() # returns array of values.

    def getAsObject(self):
        return self.__dict__ # returns object.

    def rename(self: object, newName: str):
        if self.name == newName:
            return False # value was not updated.
        else: 
            self.name = newName
            return True # value was updated.
        
    def repaint(self, newClr: str):
        self.clr = str(newClr).capitalize()
        return True

    def changeInsuranceCompany(self, newInsuranceComp: str):
        if self.insurance_company == newInsuranceComp:
            return False
        else:
            self.insurance_company = newInsuranceComp
            return True

car0 = Car("Test", 4146, "nissan;<model>", "BLUE", "XXNN XXX")
print("Car name: " + str(car0.name))
print("Car colur: " + str(car0.clr))
print("Car insurance: " + str(car0.insurance_company))
car0.rename("testtest")
car0.repaint("yellow")
car0.changeInsuranceCompany("LV")
print("New name:", str(car0.name))
print("New colour:", str(car0.clr))
print("New Insurance Company Selected: " + str(car0.insurance_company))

print(";".join(map(lambda x: str(x), car0.__dict__.values())))