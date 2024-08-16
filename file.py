lines= open("cspw2024txt.txt")

count = 0
everything = lines.read()

#counts lines in documents
for line in lines:
    count = count+1

print('\n Line Count: ', count)

#reads the whole file contents 

print("Everything in the txt: " , len(everything))
