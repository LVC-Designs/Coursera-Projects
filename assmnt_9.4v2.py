"""
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
    
    email = email[1]

    if email is email:
        emails[email] = emails.get(email,0)+1




most_common_email = max(emails, key=emails.get)


print(most_common_email, emails['cwen@iupui.edu'])


"""

## Correct Answer Below

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
emails = dict()

for line in handle:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

handle.close()

if emails:
    most_common_email = max(emails, key=emails.get)
    print(most_common_email, emails[most_common_email])
else:
    print("No emails found in the file.")