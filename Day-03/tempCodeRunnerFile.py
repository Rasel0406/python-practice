
def full_person (**addition):
     if addition["sex"]=="m":
        title = "Mr."
     else:
       title = "Ms."
print(f'{title} {addition["first_name"]} {addition["last_name"]}')

n =int(input())
people = []
for person in range(n):
    first_name, last_name,age =input().split()
    age = int(age)
    people.append({"first_name": first_name, "last_name": last_name, "age": age  "sex": sex.lower()})

people_sorted = sorted(people, key=lambda x:x["age"])
for person in people_sorted:
    full_person(**person)