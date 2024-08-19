import time
#directories of function calls
"""
x = list()
y = print()
z = str()
j = int()

dir(x)
dir(y)
dir(z)
dir(j)"""



#Appending A list:

"""stuff = list()

stuff.append('my balls are massive')

stuff.append('99inches in diameter scrotum')

print()
while True:
    question = input("What is so large ? ")

    answer = stuff

    print(answer)

    if question == "Your balls":
        print("You finally understand the lesson.")
    
        break"""

#List sorting, max min, sums, avg

friends = ['Jim', 'Jessica', 'Andrew', 'Brandon']

print("Friends Prior to assortion: ")
print(friends)
friends.sort()

time.sleep(2)
print('Friends after being sorted: ')
print(friends)
time.sleep(2)
print(sorted)

Numbers = [23, 87, 52, 19, 64, 38, 95, 11, 76, 42, 3, 59, 81, 27, 70, 15, 93, 48, 6, 32,
89, 54, 17, 61, 35, 98, 9, 73, 45, 1, 67, 84, 29, 56, 12, 91, 40, 78, 25, 50,
7, 83, 36, 69, 14, 97, 43, 2, 58, 31, 75, 20, 62, 86, 39, 94, 8, 51, 26, 72,
46, 4, 80, 33, 68, 16, 99, 41, 5, 60, 22, 85, 37, 92, 10, 55, 28, 74, 47, 13,
88, 34, 71, 18, 96, 44, 63, 30, 79, 21, 57, 82, 49, 65, 24, 90, 53, 77, 100]

print("This is the total length of numbers within the numbers list below: ")
print(len(Numbers))
time.sleep(2)
print("This is the maximum number in the numbers list: ")
print(max(Numbers))
time.sleep(2)
print("This is the minimum value in the numbers list: ")
print(min(Numbers))
time.sleep(2)
print("This is the total sum of all numbers within the list: ")
print(sum(Numbers))
time.sleep(2)
print("this is the average of numbers within the numbers list")
print(sum(Numbers)/len(Numbers))
time.sleep(2)




#Ask user input for numbers via while loop; collect numbers; average the numbers collected
#OG way with strings
total = 0 
count = 0 

while True:
    inp = input("Enter a number: ")

    if inp == 'done': 
        break

    value = float(inp)

    total = total + value
    count = count + 1

average = total/count

print("Average: ", average)

print('The total number of numbers you said: ', total)
print('The times you inputted a number: ', count)


time.sleep(2)
print("Now we'll do the same thing using a list")
numlist = []
while True:
    inp2 = input('Enter a number: ')
    if inp2 == 'done':
        break 
    value = float(inp2)
    numlist.append(value)

average = sum(numlist)/len(numlist)

print('Average: ' , average)


print("The numbers you inputted: ", numlist)
print('The total amount of numbers inputted: ', sum(numlist))
print('The max number you added: ', max(numlist))
print('The minimmum number added: ', min(numlist))

