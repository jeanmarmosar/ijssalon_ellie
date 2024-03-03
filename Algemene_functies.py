

def mijn_functie_1(mijn_int):
    return mijn_int ** 2
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))
    
#opzoekwerk .2f om ervoor te zorgen dat het getal 100+20 als resultaat 120 geeft ipv 102
#in de output verschijnt thans op het einde telkens 'None'
def mijn_functie_2():
    getal = 100.20
    getal_string = f"{getal:.2f}"
    geheel, decimaal = getal_string.split(".")
    print(int(geheel))
    print (int(decimaal))
    som=int(geheel)+int(decimaal)
    verschil=int(geheel)-int(decimaal)
    product=int(geheel)*int(decimaal)
    quotient=int(geheel)//int(decimaal)
    print([int(som), int(verschil), int(product), int(quotient)])
print(mijn_functie_2())



