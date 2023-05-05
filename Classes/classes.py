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

