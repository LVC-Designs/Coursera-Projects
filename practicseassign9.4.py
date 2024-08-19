name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
emails = dict()
"""

for line in handle:
    words = line.split()

    if len(words) > 1 and words[0] == "From ":
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

    handle.close()

if emails:
    most_common_email = max(email, key=emails.get())
    print(most_common_email, emails[most_common_email])
else:
    ("No emails found")


"""

for line in handle:
    words = line.split()

    
    if len(words) > 1 and words[0] == "From":
        email = words[1]
        emails[email] = emails.get(email, 0) + 1 # this will allow for the number of time a same email is seen to be added
    



most_common_email = max(emails, key=emails.get)


print(most_common_email, emails[most_common_email])























