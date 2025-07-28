from math import *
from random import *
names =["Noyon","Nadim","Amanullah","Rasel","aminur","Shahin"]
while names:
    name = choice(names)
    print("Name is: ", name)
    names.remove(name)

