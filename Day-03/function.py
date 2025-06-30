def all_sum(*numbers):
    sum=0
    for num in numbers:
       sum = sum + num
    return sum
       

total=all_sum(10,11,23,34,35,7)
print(total)