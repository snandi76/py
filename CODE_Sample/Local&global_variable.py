def CelciusToFerenhite_Converter(Celcius):
    Ferenhite = (Celcius * 9.0 / 5.0) + 32
    print ('{0}C = {1}F}'.Format(Celcius,Ferenhite))

Celcius = input("Enter any Temp in Celcius")
CelciusToFerenhite_Converter(Celcius)
