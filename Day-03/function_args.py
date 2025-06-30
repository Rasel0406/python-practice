def numbersArgs(num1,num2,*numbers):
    sum= num1*num2
    for num in numbers:
        sum= sum + num
    return sum
total= numbersArgs(10,20,30,40,50,60,70)
print(total)