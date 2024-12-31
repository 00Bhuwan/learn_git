x = input('Enter a number: ')
y = input('Enter a number: ')

def sub(x,y):
    if x>y:
        return x-y
    elif y>x:
        return y-x
    else:
        return 0

result = sub(x,y)
print(f'The subtracted value is {result}')