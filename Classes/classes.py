class Hen:
    # attributes 
    attribute1 = "Bird"
    attribute2 = "It is a hen"

    # methods with in the class

    def actions(self):
        print("The hen is a ", self.attribute1)
        print(f"you must like {self.attribute1}")


# to create an object from the class 
our_hen_object = Hen()

# we can access the object values like  this 

print(our_hen_object.attribute1)
print(our_hen_object.attribute2)

# calling the function from the class
our_hen_object.actions()


# Below is a class with the __inti__ function 
# This allows the attribute to be defined at the time of creation 
print("----------------look below for __init__ use output -------------------------")
class Car:
    def __init__(self, name,model, year,wheels):
        self.name = name 
        self.model = model
        self.year = year 
        self.wheels = wheels

    
    def neededCar(self):
        print("The car name is", self.name)
        print("The model is", self.model)
        print("The year of make is", self.year)
        print("This makes the car a ", self.wheels)


# defining the car object 

toyota = Car("TOYOTA", "ALTEZA", 2019, "4 Wheels")

toyota.neededCar()

print("For the benz object -----------")
benz = Car("Benz", "4-Matic", "2018", "4 wheels")

benz.neededCar()


