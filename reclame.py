
def Aanbieding_1():  
   #na de goede output komt ook 'None' te staan?
   #3.60 met :.2f gelukt
    mijn_diction = {
        "smaak" : "aardbei",  
        "prijs" : 4,  
        "korting" : 0.1
        }
    reclamesmaak=(mijn_diction["smaak"])
    reclameprijs=(mijn_diction["prijs"])
    reclamekorting=(mijn_diction["korting"])
    korting=(mijn_diction["prijs"])*(mijn_diction["korting"]/1)
    #bedrag na aftrek korting
    bedrag_korting=(reclameprijs)-korting
    reclame_tekst="Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak " f"{reclamesmaak} " "van " f"{reclameprijs} " "euro voor " f"{bedrag_korting:.2f}" " euro."
    print(reclame_tekst)
    
print(Aanbieding_1())


def inkomsten_totaal(inkomsten):
    #na de goede output komt ook 'None' te staan?
    inkomsten=sum([220, 430, 125, 160, 205, 90, 345])
    btw=0.09
    btwBedrag=inkomsten * btw 
    totaalBtwIn=inkomsten+btwBedrag
    resultaat="Het totaal van alle inkomsten van deze week is " f"{totaalBtwIn} " "euro waarover " f"{btwBedrag} " "euro btw betaald dient te worden."
    print(resultaat)

#om het totaal te bekomen bij het aanroepen van de functie heb ik 2 "" geplaatst om niet terug de inkomsten te moeten  ingeven
#dus print(inkomsten_totaal(inkomsten)) werkt niet 

print(inkomsten_totaal(""))

def laag_en_hoog(mijn_lijst):
    #na de goede output komt ook 'None' te staan?
    mijnInkomsten=[220, 430, 125, 160, 205, 90, 345]
    Laagste=min([220, 430, 125, 160, 205, 90, 345])
    Hoogste=max([220, 430, 125, 160, 205, 90, 345])
    print(Laagste, Hoogste)
    
print(laag_en_hoog(""))


def gemiddelde(Mijn_lijst):
    #na de goede output komt ook 'None' te staan?
    
    Mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
    aantal=len(Mijn_lijst)
    GemVerkoop=sum(Mijn_lijst)/aantal
    #print(GemVerkoop)
    GemiddeldeInkomstenDezeWeek = "De gemiddelde inkomsten deze week zijn " f"{GemVerkoop:.0f} ""euro."
    print(GemiddeldeInkomstenDezeWeek)
print(gemiddelde(""))


    



 

    

 
    
    


    