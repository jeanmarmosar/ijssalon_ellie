

from helper import *
from presentatie import presenteer
import csv

Dic_Inkomsten   = {
    'Aardbeien-ijs-totaal' : 1000, 
    'Vanille-ijs-totaal': 2000, 
    'Chocolade-ijs-totaal' : 1500, 
    'Waterijsjes-totaal' : 750
    }

totaal_inkomsten=som(Dic_Inkomsten)
#print(totaal_inkomsten)

presenteer(Dic_Inkomsten,totaal_inkomsten)

#???
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in Dic_Inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])