import time

name = input("Enter file:")


if len(name) < 1:
    name = "mbox-short.txt"


handle = open(name)

emails = dict()

for line in handle:
    line = line.rstrip()


    
    

    if not line.startswith("From "):
        email = line.split()
        continue

    email = line.split()

    #print("These are the words" , words)
    
    email = email[1]



    #print(email)

    if email is email:
        emails[email] = emails.get(email,0)+1 


#print(emails)

most_common_email = max(emails, key=emails.get)


print(most_common_email, emails['cwen@iupui.edu'])
   
   