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