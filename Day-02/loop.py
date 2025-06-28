animals =["cat","dog","rabbit","elephant","lion","tiger","bear","zebra"]
for x in animals:
    if x=="gorilla":
        print("Gorilla is not in the list")
    elif x=="bison":
        print("Bison is not in the list")
    elif x in animals[2:5]:
          print("Found a animal in the list",x)
          continue
    elif x == animals[3]:
        print("This is not a gorilla or bison, it is a elephant")

   