import time

counts = dict()

print("Entah a linah textah: ")

line = input('Write hither; ')

words = line.split()

print('Words: ', words)

print("Counting. . . ")

time.sleep(5)

for word in words:
    counts[word] = counts.get(word,0) + 1

print('Counts', counts)



for key in counts:
    print(key, counts[key])

time.sleep(1)
print(list(counts))
time.sleep(1)

time.sleep(1)
print(list(counts.keys()))#gets the keys in a dict and throws the keys in a list
time.sleep(1)

time.sleep(1)
print(list(counts.values()))#gets the values in the dict and throws in a list
time.sleep(1)

time.sleep(1)
print(list(counts.items()))# gets each item; in each dictionery, and gets the Tuple, tuple is kinda like a read only list, they are just lists that ARE TWO things in order
time.sleep(1)

time.sleep(1)
bigcount = None
bigword = None

for word, count in counts.items():
    print(word, count)
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

time.sleep(1)
time.sleep(1)
print("This is the biggest word" , bigword, bigcount)



"""
Summary:
- Whats a collection
- Lists versus dictionaries
- Dictionary Constants
- The most common word
= Using the get() method
- Writing dictionary loops
- Sneak peek: Tuples 

"""