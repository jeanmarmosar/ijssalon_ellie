
#functies oefenopgaven les 8
def mijn_functie(mijn_int): 
    return mijn_int * 2

print(mijn_functie(2))

b = 15
def mijn_functie():
    global b
    b = b + 10
    print("binnen: ", b)

print("buiten: ", b)
mijn_functie()
print("buiten: ",b)


def mijn_functie(mijn_lijst):
    totaal = 0 
    for nr in mijn_lijst:    
        totaal += nr 
    return totaal
print(mijn_functie([12,5,3]))

#voor elke variabele c in string1 die voorkomt in string 2, toon die variabele
def mijn_functie(string1, string2): 
    uitvoer = "" 
    for c in string1:    
        if c in string2:       
            uitvoer += c 
    return uitvoer
print(mijn_functie("jean-marc","mosar"))

#b is hier gewoon een parameter
a = 10
b = 20
def maal_drie(b):  
    return b * 3
print(maal_drie(a))

#a is hier gewoon een parameter, ook wordt global gebruikt
a = 10
b = 20
def maal_drie(a):  
    global b  
    return b * 3
print(maal_drie(20))

#----------
a = 10
def maal_drie(a):  
    return a * 3

def mijn_functie(a):  
    a = maal_drie(a)  
    uitvoer = maal_drie(a)  
    return uitvoer * 2
print(mijn_functie(20))




