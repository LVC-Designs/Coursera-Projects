print("Now we'll do the same thing using a list")
numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break 
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)

print('Average: ' , average)


print("The numbers you inputted: ", numlist)
print('The total amount of numbers inputted: ', sum(numlist))
print('The max number you added: ', max(numlist))
print('The minimmum number added: ', min(numlist))
