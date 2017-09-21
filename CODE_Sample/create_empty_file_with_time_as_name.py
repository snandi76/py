import os
import datetime

filename = datetime.datetime.now()

def create_file():
    with open(str(filename.strftime("%y-%m-%H")),'w') as file:
        file.write()#write empty string

create_file()
