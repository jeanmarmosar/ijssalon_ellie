
def Aanbieding_1():  
   #na de goede output komt ook 'None' te staan
   #3.6 moet 3.60 worden, via round lukt het niet
    mijn_diction = {
        "smaak" : "aardbei",  
        "prijs" : 4,  
        "korting" : 0.1
        }
    reclamesmaak=(mijn_diction["smaak"])
    reclameprijs=(mijn_diction["prijs"])
    reclamekorting=(mijn_diction["korting"])
    korting=(mijn_diction["prijs"])*(mijn_diction["korting"]/1)
    bedrag_korting=(reclameprijs)-korting
    reclame_tekst="Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak " f"{reclamesmaak} " "van " f"{reclameprijs} " "euro voor " f"{bedrag_korting}" " euro."
    print(reclame_tekst)
    
print(Aanbieding_1())