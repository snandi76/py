def CelciusToFerenhite_Converter(Celcius):
    Ferenhite = (Celcius * 9.0 / 5.0) + 32
    return '{0}C = {1}F'.format(Celcius,Ferenhite)


#Celcius = float(input("Enter any Temp in Celcius"))
temperatures=[10,-20,-289,100]
ListOfConversion = list()
for temp in temperatures:
    Celcius = temp
    if(Celcius >= -273.15):
        ListOfConversion.append(CelciusToFerenhite_Converter(float(Celcius)))
print(ListOfConversion)
with open('tempConversionFile.txt','a+') as file:
    for str in ListOfConversion:
        file.write(str+'\n')
