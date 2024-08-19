"""ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['csev'] = ccc['csev'] + 1
print(ccc)

"""

counts = dict()

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1 # this adds a new name and puts a single tick; essentially
    else:
        counts[name] = counts[name] + 1 #since its in there, we add the count for the amount of names within the counts

print(counts)

#this captures the moment, when we run into a name; the dictionary becomes a histogram of the counts of word

"""
#The get method for dictionaries
- The pattern of checking to see if a key is already in a dictionary
- Assuming a default value if the key is not there is so common that there is a method called get() that does this for us
"""

if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

print(x)
print(y)


counts = dict()

for name in names:
    counts[name] = counts.get(name,0)+1

print(counts)