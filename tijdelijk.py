mijn_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5,
}

#print(mijn_dictionary["aardbei"] * 0.8)
#keys = mijn_dictionary.keys()
#values = mijn_dictionary.values()
#print(keys)
#print(values) cc
aanbieding= round(mijn_dictionary["aardbei"]*0.8,2)
reclame_tekst="Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € "
reclame_tekst2 = reclame_tekst + str(aanbieding)
reclame_tekst3=(reclame_tekst2.upper())
reclame_tekst4=reclame_tekst3.split(" ")
#print(reclame_tekst4)
for el in reclame_tekst4 :  
    #print(el)
    if len (el) >=5:
        print(el.upper())
    else:
       print(el.lower()) 