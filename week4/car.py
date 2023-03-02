class car:
    def __init__(self,model,manufacturer,colour,capacity,yearo):
        self.model=model
        self.manufacturer=manufacturer
        self.colour=colour
        self.capacity=capacity
        self.yearo=yearo


# setters and getters
#setters used to set attribute
#getters used to get attributes

#getters
    def get_model(self):
        return self.model
    def get_manufacturer(self):
        return self.manufacturer
    def get_yearo(self):
        return self.yearo
#setters
    def set_model(self,model):
        self.model=model
    def set_manufacturer(self,manufacturer):
        self.manufacturer=manufacturer
    def set_yearo(self,yearo):
        self.yearo=yearo
    
#objects
car1=car("demio","nissan","red",1300,2016)
car2=car("mustang","ford","black",4500,2008)
car3=car("pagera","ferrari","white",3500,2018)

#getting attributes
print(car1.get_model())
print(car1.get_manufacturer())
print(car1.get_yearo())
print(car2.get_model())
print(car2.get_manufacturer())
print(car2.get_yearo())

#how to set 
car1.set_yearo(2021)
car2.set_yearo(1985)

print(car1.get_yearo())
print(car2.get_yearo())





