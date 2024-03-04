
def Aanbieding_1():  
   #na de goede output komt ook 'None' te staan
   #3.60 met :.2f gelukt
    mijn_diction = {
        "smaak" : "aardbei",  
        "prijs" : 4.00,  
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