Maillist = ["sun@gmail.com","m@yahoo.com", "titly@gmail"]

for mailaddr in Maillist:
    if 'gmail' in mailaddr:
        print(mailaddr)
    else:
        continue
        #print("Not gmail address")
