#Control Structures and Functions

#if ...else
num = int(input('Enter a number:'))
if num %2 == 0:
    print('it is an even number')
elif num > 0:
    print('it is a positive number')
else: print('it is an odd negative number')


#for loop
sum = 0
marks = [21,25,20,18,24]
for i in marks:
    sum += i
else: print('No numbers left')
print('marks',marks)
print('sum:',sum)


#while loop
limit = int(input('Enter a number:'))
i = 0
while(i <= limit):
    i += 1
    print(i)


#break & continue
name = 'abhinav'
for i in name:
    if i == 'i':
        break                           #breaks the current function,goes to next line
    print(i)

for i in name:
    if i == 'i':
        continue                        #breaks the current function,goes to start of function
    print(i)


#functions
def multiply(num):                      #def is uesd to define a function
    for i in range(1,11):
        print(num,'*',i,'=',num*i)
num2 = int(input('Enter a number:'))
multiply(num2)



