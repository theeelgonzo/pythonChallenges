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
"""

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
