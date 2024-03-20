import math

def tel_op(a,b):  
    return a + b
    
totaal = tel_op(5,10)
print(totaal)

def mijn_functie_1(a):
    return a * a
print(mijn_functie_1(2))


def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
print(mijn_functie_2(2,4))

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.'''
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))



def inkomsten_totaal(inkomsten,btw):
    
    totaal = 0
    btw=0.21
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
     
        uitvoer = f'''Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.'''
        return uitvoer
print(inkomsten_totaal([10,5,3,2,1,2,9], 0.21))

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer
print(laag_en_hoog([10,5,3,2,1,2,9]))

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer    
print(combinatie([10,5,3,2,1,2,9]))


global leeft
def over_2_jaar():    
    leeft=10
    leeft=leeft+2
    return leeft

print(over_2_jaar())


getal1 = input("Wat is getal 1? ")
getal2 = input("Wat is getal 2? ")
uitkomst = int(getal1) + int(getal2)
print(f"{getal1} + {getal2} = {uitkomst}")



def pi():   
    return 3.1415
radius = 2
oppervlakte = pi() * (radius ** 2)
print (oppervlakte)


#hard coding
def discriminant(a,b,c):    
    # voor: ax^2 + bx + c    
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)    
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)    
    uitvoer = [D1,D2]    
    return uitvoer
#print("Voor de formule ax^2 + bx + c, geef a , b en c:")
#a = int(input("Wat is a? "))
#b = int(input("Wat is b? "))
#c = int(input("Wat is c? "))
print("Voor de formule ax^2 + bx + c, geef a , b en c:")
a = -3 #int(input("Wat is a? "))
b = 2 #int(input("Wat is b? "))
c = 5 #int(input("Wat is c? "))
#uitkomst = discriminant(a,b,c)
#D1 = uitkomst[0]
#D2 = uitkomst[1]
#print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn :")
#print(f"{D1} en {D2}")
uitkomst = discriminant(a,b,c)
D1 = uitkomst[0]
D2 = uitkomst[1]
print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn :")
print(f"{D1} en {D2}")