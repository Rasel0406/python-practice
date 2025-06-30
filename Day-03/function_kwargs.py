def full_name(first,Last,**addition):
    name =f'Full name: {first} {Last}'
    #print(addition["home_address"])
    for key, value in addition.items():
       # print(key,':',value)
        name += f', {key}: {value} \n'
      
    return name
name = full_name("Rasel", "Miah", age=25, city="Dhaka", country="Bangladesh",zip_code=1212,home_address="Mohakhali")
print(name)
    