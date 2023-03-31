# given two integer numbers, return their product if the product is less than or
# equal to 1000, otherwise return their sum

def prodOrSum(num1, num2):
    product = num1 * num2
    total = num1 + num2
    if product <= 1000:
        print(f'The result is {product}')
    else:
        print(f'The result is {total}')

prodOrSum(20, 30)
prodOrSum(40, 30)
