text = "X-DSPAM-Confidence:    0.8475"

count = 0 
#for x in text:
  #  print(count, x)
   # count = count + 1

pos = text.find(":")


print(pos)

answer = text[pos+1:].strip()

print(answer)