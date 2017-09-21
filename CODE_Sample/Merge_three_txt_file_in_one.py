import glob2
import datetime

def func():
    listOfFile = glob2.glob("Sample-Files\\*.txt")
    ListOfFileData = []
    with open(str(datetime.datetime.now().strftime("%y-%m-%H-%M-%S-%f")),'a+') as NewFile:
        for filename in listOfFile:
            with open(filename,'r') as file:
                NewFile.write(file.read())


func()
