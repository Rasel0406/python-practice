N = int(input("Number of operations: "))
my_list=[]
for lists in range(N):
   cmd = input().strip().split()
   operation =cmd[0]
   if operation == "insert":
      index,value = int(cmd[1]), int(cmd[2])
      my_list.insert(index, value)
   elif operation == "print":
      print(my_list)
   elif operation == "remove":
      value = int(cmd[1])
      my_list.remove(value)
   elif operation == "append":
        value = int(cmd[1])
        my_list.append(value)
   elif operation == "sort":
      my_list.sort()
   elif operation == "pop":
      my_list.pop()
   elif operation == "reverse":
      my_list.reverse()         
      
print(my_list)
 