salary = 8000

def printSalary():
    salary = 500
    print('salary', salary)

printSalary()

print('salary', salary)

# reversing an interger

value= int(input('Please enter a number '))
print('The value entered was %a'%value)
n = 0
while value!=0:
    n = n*10 + value%10
    print(n)
    value = value//10

print(f'When reversed the number is {n}')


x = [1,2,3,4]
y = [sum(x[0:a+1]) for a in range(0, len(x))]
print(y)
print(x[0:1], 'returned list')

print(sum([1,2]))

# How sum function works 
list_value = [3, 3, 4]

print(sum(list_value, 100))