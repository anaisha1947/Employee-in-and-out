#Write a program to create a class with the named employee and 
# create a constructor and destructor. 
# Then, write a function to create an object for that class and 
# delete the object. 
# Make sure you call the function to get everything implemented!
class Employees:
    def __init__(self, name):
        self.name = name
    def signed_in(self):
        print(f"{self.name} signed in.")
    def signed_out(self):
        print(f"{self.name} signed out.")
e = Employees("Raghav")
e.signed_in()
e.signed_out()
del e