# given two integer numbers, return their product if the product is less than or
# equal to 1000, otherwise return their sum
"""
def prodOrSum(num1, num2):
    product = num1 * num2
    total = num1 + num2
    if product <= 1000:
        print(f'The result is {product}')
    else:
        print(f'The result is {total}')

prodOrSum(20, 30)
prodOrSum(40, 30)


#write a program to iterate the first 10 numbers and in each iteration print the
# sum of the previous and the current numbers

#Printing current and previous number sum in a range(10)
#Current Number # Previous Number # Sum: #

curNum = 0
prevNum = 0
print('Printing current and previous number sum in a range(10)')
for i in range(10):
    total = curNum + prevNum
    print(f'Current number {curNum} Previous number {prevNum} Sum: {total}')
    prevNum = curNum
    curNum += 1

# Original string is pynative
# Printing only even index characters

#userString = input()
samString = 'pynative'

print('Original String is pynative')
print('Printing only even index characters')
for i in range(len(samString)):
    if i % 2 == 0:
        print(samString[i])

userString = input('Please provide a string')
print(f'User string is: {userString}')
print('Printing only even index characters')
for i in range(len(userString)):
    if i % 2 == 0:
        print(userString[i])


#write a program to remove characters in a string from 0 up to n and 
#return a new string.
#NOTE: N MUST BE LESS THAN THE LENGTH OF THE STRING

def removeChars(string, n):
    if n >= len(string):
        print('The number must be less than the length of your string!')
    else:
        newString = string[n:]
        print(newString)

removeChars('pynative', 4)
removeChars('pynative', 2)
removeChars('batman', 2)
removeChars('batman', 10)

#check to see if first and last number of a list are the same
#given list [abcd] result is true
#give list [efgh] reseult is false

list1 = [1, 2, 3, 4, 5, 1]
list2 = [10, 20, 30, 40, 50, 10]
list3 = [3, 4, 5]
list4 = [7, 1, 4, 10, 999, 11]

def checkList(x):
    if type(x) != list:
        print('Provide a list...or else, yarko!')
    else:
        if x[0] == x[len(x)-1]:
            print(f'Given list {x} the result is true!')
        else:
            print(f'Given list {x} the result is false!')
checkList(list1)
checkList(list2)
checkList(list3)
checkList(list4)
"""
# iterate over a given list of numbers and print only those divisibly by 5
#given list is a b c d e f
#divisible by 5
# d
# e
# f
numList = [10, 20, 33, 46, 55]
print(f'Given list is {numList}')
print('Divisible by 5:')
for num in numList:
    if num % 5 == 0:
        print(num)

# write a program to see how many times the substring 'emma' appears in given
# string
# Emma appeared 2 times
strX = 'Emma is a good developer. Emma is a writer.'
print('Emma appeared ', strX.count('Emma'), 'times!')

for num in range(1, 6):
    print(str(num) * num)

# write program to check if three digit number is palindrome number
#original number 121/125
# yes/no, given number is/is not palindrome number
num1 = 121
num2 = 125

def checkPal(number):
    print(f'Original number is {number}')
    strNum = str(number)
    revNum = strNum[::-1]
    print(int(revNum))
    if list(revNum)[0] == list(strNum)[0]:
        print('Yes, given number is palindrome number')
    else:
        print('No, given number is not palindrome number')

checkPal(num1)
checkPal(num2)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60,  75, 90]
list3 = []
# odd from first, even from second
for num in list1:
    if num % 2 != 0:
        list3.append(num)
for num in list2:
    if num % 2 == 0:
        list3.append(num)
print(list3)
 
 # extract digits from 7536 in reverse order and add space
digit = 7536
revDig = ' '.join(str(digit)[::-1])
print(revDig)

x = 1
y = 1
for i in range (1, 11):
    for j in range (1, 11):
        k = j * i
        print(k, end=' ')
    print('\t\t')
