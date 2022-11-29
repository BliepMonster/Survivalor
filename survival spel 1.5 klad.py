import random
speleindigen = 0
wetenschapstafel = 0
aantalkoper = 0
aantalhout = 0
aantalblad = 0
aantalfruit = 0
aantalivoor = 0
aantalkleinvlees = 0
aantalgewoonvlees = 0
aantalgrootvlees = 0
aantalbrood = 0
aantalsteen = 0
stenenhouweel = 0
starterhut = 0
aantalfruittaart = 0
aantalijzer = 0
aantalgekooktkleinvlees = 0
aantalgekooktgewoonvlees = 0
aantalgekooktgrootvlees = 0
aantalgeneeskrachtigekruiden = 0
ijzerenhouweel = 0
honger = 10
krachtxp = 0
krachtlevel = 0
oudehp = 20
oudedamage = 2
nieuwedamage = 2
grotlevel = 0
wetenschapsxp = 0
wetenschapslevel = 0
zombiehp = 15
hpverloren = 0
zombietegengekomen = 0
stenenzwaard = 0
ijzerenzwaard = 0
zombiezwaard = 0
aantaldiamant = 0
gehoorndehelm = 0
aantalvis = 0
hp = 0
maxhp = 20
stenenbijl = 0
ijzerenbijl = 0
zeis = 0
aantalgraan = 0
koeienkudde = 0
schapenkudde = 0
varkenkudde = 0
stal = 0
boerderij = 0
graancyclus = 0
bakkerij = 0
krachtdrank = 0
hpdrank = 0
hongerdrank = 0
effect = 0
drankkracht = 0
drankhp = 0
drankhonger = 1
eftijd = 0
goud = 0
aantalaluminium = 0
geautomatiseerdeoven = 0
voertijd = 0
autoboomgaard = 0
boomgaardtijd = 0
vishengel = 0
class Farmer():
    def __init__(self,name):
        self.name = name
    #Instance method
        def voorstellen(self):
            return f'Boer {self.name}: Halt! Dit is mijn boerderij. Ga nu meteen weg!' 
jeff = Farmer('Jeff')
bart = Farmer('Bart')
class Animal():
    def __init__(self,species,drop):
        self.species = species
        self.drop = drop
    #Instance method
        def tegenkomen(self):
            return f'Je bent een groep {self.species} tegengekomen!'
    #Another instance method
        def slachting(self):
            return f'Je kudde {self.species} is gestorven en liet een {self.drop} achter!'
koe = Animal('koeien','groot vlees')
schaap = Animal('schapen','gewoon vlees')
varken = Animal('varkens','groot vlees')
class experimenten():
    def __init__(self,experiment):
        self.experiment=experiment
    #Instance method
        def q(self):
            return f'Je hebt {self.experiment}.'
ea = experimenten('water en klei gemengd en gekeken wat er gebeurt')
eb = experimenten('een dier opengesneden')
ec = experimenten('een zuur met een base gemengd')
commandos = ["Houthakken", "Jagen", "Verkennen", "Maken", "Bouwen", "eten", "inventaris", "recepten", "toverdrank drinken"]
spelenjaofnee = input("Welkom bij mijn spel! Zeg start om het spel te starten.")
if spelenjaofnee == "start" or spelenjaofnee == "Start" or spelenjaofnee == "starten" or spelenjaofnee == "Starten":
    print("Je bent gestrand in het midden van het oerwoud. Het enige wat je hebt is een rots.")
    while speleindigen == 0:
        if koeienkudde == 1 or varkenkudde == 1 or schapenkudde == 1:
            voertijd += 1
        if voertijd == 10:
            aantalgraan -= 3
            if not koeienkudde == 1:
                aantalgraan += 1
            else:
                aantalgrootvlees += 1
                koe.slachting()
            if not varkenkudde == 1:
                aantalgraan += 1
            else:
                aantalgrootvlees += 1
                varken.slachting()
            if not schapenkudde == 1:
                aantalgraan += 1
            else:
                aantalgewoonvlees += 1
                schaap.slachting()
                voertijd = 0
        if wetenschapsxp == 4 and wetenschapslevel == 0:
            print('Wetenschapslevel is nu 1!')
            wetenschapslevel += 1
            wetenschapsxp = 0
        elif wetenschapsxp == 10 and wetenschapslevel == 1:
            print('Wetenschapslevel is nu 2!')
            wetenschapslevel += 1
            wetenschapsxp = 0
        elif wetenschapsxp == 20 and wetenschapslevel == 2:
            print('Wetenschapslevel is nu 3!')
            wetenschapslevel += 1
            wetenschapsxp = 0
        elif wetenschapsxp == 50 and wetenschapslevel == 3:
            print('Wetenschapslevel is nu 4!')
            wetenschapslevel += 1
            wetenschapsxp = 0
        if autoboomgaard == 1:
            boomgaardtijd += 1
            if boomgaardtijd == 5:
                aantalfruit += 3
                boomgaardtijd = 0
        if boerderij == 1:
            graancyclus += 1
            if graancyclus == 5:
                aantalgraan += 2
                graancyclus = 0
        if effect == 1:
            eftijd += 1
            if eftijd == 10:
                eftijd = 0
                effect = 0
                if drankkracht >= 1:
                    drankkracht = 0
                if drankhp >= 1:
                    drankhp = 0
                if drankhonger >= 2:
                    drankhonger = 1
        honger -= 1/drankhonger
        if honger == 0:
            quit()
        elif honger > 9:
            honger = 9
        print("Je hebt", honger, "honger. Als honger op 0 komt, sterf je!")
        if krachtxp == 10 and oudedamage == 2:
            oudedamage = 3
            print("Gefeliciteerd! Je krachtlevel is nu 1!")
            krachtlevel = 1
        elif krachtxp == 50 and oudedamage == 3:
            oudedamage = 4
            print("Gefeliciteerd! Je krachtlevel is nu 2")
            krachtlevel = 2
        elif krachtxp == 200 and oudedamage == 4:
            oudedamage = 5
            print("Gefeliciteerd! Je krachtlevel is nu 3")
            krachtlevel = 3
        if zombiezwaard == 1:
            nieuwedamage = oudedamage+5+drankkracht
        elif ijzerenzwaard == 1:
            nieuwedamage = oudedamage+2+drankkracht
        elif stenenzwaard == 1:
            nieuwedamage = oudedamage+1+drankkracht
        else:
            nieuwedamage = oudedamage+drankkracht
        if gehoorndehelm == 1:
            hp = oudehp+5+drankhp
            maxhp = 25+drankhp
        else:
            hp = oudehp+drankhp
        if geautomatiseerdeoven == 1:
            aantalgekooktkleinvlees += aantalkleinvlees
            aantalkleinvlees = 0
            aantalgekooktgewoonvlees += aantalgewoonvlees
            aantalgewoonvlees = 0
            aantalgekooktgrootvlees += aantalgrootvlees
            aantalgrootvlees = 0
        actie = input("Wat zou je willen doen? Typ commandos voor een lijst van alle commando's.")
        if hp+5 > maxhp and aantalgeneeskrachtigekruiden >= 1:
            aantalgeneeskrachtigekruiden -= 1
            hp += 5
        if actie == "commandos" or actie == 'c':
            print("De huidige commando's zijn:", commandos)
            honger += 1/drankhonger
        elif actie == "houthakken" or actie == 'h':
            mogelijkehouthakitems = ['Hout', 'blad', 'fruit']
            n = random.randint(0,2)
            if n == 0:
                a = 'Hout'
                aantalhout += 1
            elif n == 1:
                a = 'blad'
                aantalblad += 1
            else:
                a = 'fruit'
                aantalfruit += 1
            print(a)
            n = random.randint(0,3)
            if n == 1:
                n = random.randint(0,2)
                if n == 0:
                    a = 'Hout'
                    aantalhout += 1
                elif n == 1:
                    a = 'blad'
                    aantalblad += 1
                else:
                    a = 'fruit'
                    aantalfruit += 1
                print(a)
            if ijzerenbijl == 1:
                aantalhout += 2
            elif stenenbijl ==1:
                aantalhout += 1
            krachtxp += 1
        elif actie == 'jagen' or actie == 'j':
            n = random.randint(0,3)
            if n == 0:
                a = 'ivoor'
                aantalivoor += 1
            elif n == 1:
                a = 'klein vlees'
                aantalkleinvlees += 1
            elif n == 2:
                a = 'vlees'
                aantalgewoonvlees += 1
            else:
                a = 'groot vlees'
                aantalgrootvlees += 1
            print(a)
            n = random.randint(0,4)
            if n == 1:
                n = random.randint(0,3)
                if n == 0:
                    a = 'ivoor'
                    aantalivoor += 1
                elif n == 1:
                    a = 'klein vlees'
                    aantalkleinvlees += 1
                elif n == 2:
                    a = 'vlees'
                    aantalgewoonvlees += 1
                else:
                    a = 'groot vlees'
                    aantalgrootvlees += 1
                print(a)
        elif actie == 'verkennen' or actie == 've':
            n = random.randint(0,9)
            if n == 1:
                n = random.randint(1,3)
                aantalbrood += n
                print("Je hebt", n, "broden gevonden in een verlaten stad")
            elif n == 2 or n == 3 or n == 4:
                n = random.randint(1,4)
                aantalsteen += n
                print("je hebt", n, "stenen gevonden")
            elif n >= 6:
                aantalgeneeskrachtigekruiden += 1
                print("Je hebt wat geneeskrachtige kruiden gevonden.")
            elif n == 7 and zeis == 1:
                n = random.randint(0,1)
                if n == 0:
                    n = random.randint(1,5)
                    print("Je hebt een verlaten boerderij gevonden en", n, "graan meegenomen")
                    aantalgraan += n
                else:
                    print("Je hebt een boerderij tegengekomen!")
                    n = random.randint(0,1)
                    if n == 0:
                        jeff.voorstellen()
                    else:
                        bart.voorstellen()
                    zombiedood = 0
                    if zombietegengekomen == 0:
                        print("Hier een kort hulptekstje over gevechten. Je kan alles wat een vijand doet aflezen op het scherm. Als hij aan het afwachten is, druk dan op A. Als hij aan het aanvallen is, druk dan op B.")
                    while zombiedood == 0:
                        aanval = random.randint(0,1)
                        if aanval == 0:
                            print("afwachten")
                            toetsingedrukt = input()
                            if toetsingedrukt == 'a':
                                hpverloren= random.randint(0,3)
                                print("hp verloren:", hpverloren, "schade gedaan:", nieuwedamage)
                                zombiehp -= nieuwedamage
                                hp -= hpverloren
                            else:
                                print("Je hebt de verkeerde toets ingedrukt")
                        else:
                            if toetsingedrukt == 'b':
                                print("Je hebt niets verloren en ook geen schade gedaan.")
                            else:
                                hpverloren = random.randint(1,3)
                                print("Je hebt de verkeerde toets ingedrukt en", hpverloren, "HP verloren.")
                        if zombiehp == 0:
                            zombiedood = 1
                            print("Gefeliciteerd! Je hebt de vijand gedood!")
                            zombietegengekomen += 1
                            n = random.randint(1,10)
                            print("Je hebt de boerderij geplunderd en", n, "graan meegenomen")
                            aantalgraan += n
            elif n == 8:
                n = random.randint(0,2)
                if n == 0:
                    koe.tegenkomen()
                    meenemen = input('Wil je ze meenemen? Let op: je moet een stal hebben en ze gebruiken 1 graan elke 10 beurten')
                    if 'j' in meenemen and stal == 1:
                        koeienkudde += 1
                elif n == 1:
                    schaap.tegenkomen()
                    meenemen = input('Wil je ze meenemen? Let op: je moet een stal hebben en ze gebruiken 1 graan elke 10 beurten')
                    if 'j' in meenemen and stal == 1:
                        schapenkudde += 1
                else:
                    varken.tegenkomen()
                    meenemen = input('Wil je ze meenemen? Let op: je moet een stal hebben en ze gebruiken 1 graan elke 10 beurten')
                    if 'j' in meenemen and stal == 1:
                        varkenkudde += 1
            elif n == 9:
                n = random.randint(0,99)
                if n == 0:
                    print('Op een dag, in het oerwoud, kwam je een verlaten hut tegen...')
                    print('Toen je naar binnen keek, zag je een tovenaar spreuken zeggen.')
                    watdoen = input('Wat ga je doen? a) naar binnen gaan, en b) wegvluchten')
                    if watdoen == a:
                        print("Je ging naar binnen en... Hij was helemaal niet vijandig! Hij begroette je vriendelijk en vroeg of je iets wou kopen!")
                        kopen = input('Wil je iets kopen?')
                        if kopen == 'ja':
                            print("Tovenaar: 'Ik verkoop:")
                            print("Toverdranken en betoveringen!'")
                            watkopen = input('Welk van de twee wil je kopen?')
                            if watkopen == 'toverdrank':
                                print("Tovenaar: 'Ik verkoop de volgende toverdranken:")
                                print("Kracht, hp, en honger!'")
                                watkopen = input('Welk van de drie wil je?')
                                if watkopen == 'kracht':
                                    print('Dat kost 10 goud.')
                                    print('Wil je het nog steeds kopen?')
                                    kopen = input()
                                    if kopen == 'ja':
                                        if goud >= 10:
                                            goud -= 10
                                            krachtdrank += 1
                                        else:
                                            print('Je hebt niet genoeg goud.')
                                elif watkopen == 'hp':
                                    print('Dat kost 10 goud.')
                                    print('Wil je het nog steeds kopen?')
                                    kopen = input()
                                    if kopen == 'ja':
                                        if goud >= 10:
                                            goud -= 10
                                            hpdrank += 1
                                        else:
                                            print('Je hebt niet genoeg goud.')
                                elif watkopen == 'honger':
                                    print('Dat kost 10 goud.')
                                    print('Wil je het nog steeds kopen?')
                                    kopen = input()
                                    if kopen == 'ja':
                                        if goud >= 10:
                                            goud -= 10
                                            hpdrank += 1
                                        else:
                                            print('Je hebt niet genoeg goud.')
                            elif watkopen == 'betovering':
                                print("Tovenaar: 'Ik ken maar 1 betovering, en dat is die van kracht. Hij kost 15 goud.'")
                                kopen = input('Wil je hem kopen?')
                                if kopen == 'ja':
                                    if goud >= 15:
                                        goud -= 15
                                        nieuwedamage += 1
                                    else:
                                        print('Je hebt niet genoeg goud.')
                elif n == 2:
                    print('Je bent een verlaten bibliotheek tegengekomen. Je las alle boeken en ging toen weg.')
                    wetenschapsxp += 25
            else:
                print("Je had pech en hebt niets gevonden")
        elif actie == 'maken' or actie == 'ma':
            maakbareitems = []
            if aantalhout >= 2 and aantalsteen >= 3:
                maakbareitems.append('stenen houweel')
                maakbareitems.append('stenen zwaard')
                maakbareitems.append('stenen bijl')
            if aantalhout >= 2 and aantalijzer >= 3:
                maakbareitems.append('ijzeren houweel')
                maakbareitems.append('ijzeren zwaard')
                maakbareitems.append('ijzeren bijl')
                maakbareitems.append('zeis')
            if aantalhout >= 4 and aantalivoor >= 5:
                maakbareitems.append('gehoornde helm')
            if aantalkoper >= 3 and goud >= 2 and aantalijzer >= 15:
                maakbareitems.append('wetenschapstafel')
            if aantalkoper >= 5 and goud >= 3 and aantalaluminium >= 20 and aantaldiamant >= 1 and starterhut == 1:
                maakbareitems.append('geautomatiseerde oven')
            if aantalkoper >= 2 and goud >= 1 and wetenschapslevel >= 1:
                maakbareitems.append('aluminium')
            if aantalkoper >= 10 and goud >= 10 and aantaldiamant >= 3 and aantalaluminium >= 25 and wetenschapslevel >= 5:
                maakbareitems.append('geautomatiseerde boomgaard')
            if aantalhout >= 3 and aantalblad >= 2:
                maakbareitems.append('vishengel')
            print("je kan het volgende maken:", maakbareitems)
            itemgemaakt = input()
            if itemgemaakt in maakbareitems:
                if itemgemaakt == 'ijzeren houweel':
                    aantalijzer -= 3
                    aantalhout -= 2
                    ijzerenhouweel = 1
                elif itemgemaakt == 'stenen houweel':
                    aantalhout -= 2
                    aantalsteen -= 3
                    stenenhouweel = 1
                    commandos.append('mijnwerken')
                    print('Nieuw commando ontdekt!')
                elif itemgemaakt == 'stenen zwaard':
                    aantalsteen -= 3
                    aantalhout -= 2
                    stenenzwaard = 1
                elif itemgemaakt == 'ijzeren zwaard':
                    aantalhout -= 2
                    aantalijzer -= 1
                    ijzerenzwaard = 1
                elif itemgemaakt == 'gehoornde helm':
                    aantalhout -= 4
                    aantalivoor -= 5
                    gehoorndehelm = 1
                elif itemgemaakt == 'stenen bijl':
                    aantalhout -= 2
                    aantalsteen -= 3
                    stenenbijl = 1
                elif itemgemaakt == 'ijzeren bijl':
                    aantalhout -= 2
                    aantalijzer -= 3
                    ijzerenbijl = 1
                elif itemgemaakt == 'zeis':
                    aantalhout -= 2
                    aantalijzer -= 3
                    zeis = 1
                elif itemgemaakt == 'wetenschapstafel':
                    aantalijzer -= 15
                    aantalkoper -= 3
                    goud -= 2
                    wetenschapstafel = 1
                    commandos.append('experimenteren')
                    print('Nieuw commando ontdekt!')
                elif itemgemaakt == 'geautomatiseerde oven':
                    aantalaluminium -= 20
                    aantalkoper -= 5
                    goud -= 3
                    aantaldiamant -= 1
                    geautomatiseerdeoven = 1
                elif itemgemaakt == 'aluminium':
                    aantalkoper -= 2
                    goud -= 1
                    aantalaluminium += 3
                elif itemgemaakt == 'geautomatiseerde boomgaard':
                    aantalkoper -= 10
                    goud -= 10
                    aantaldiamant -= 3
                    aantalaluminium -= 25
                    autoboomgaard = 1
                elif itemgemaakt == 'vishengel':
                    aantalhout -= 3
                    aantalblad -= 2
                    vishengel = 1
                    commandos.append('vissen')
                    print('Nieuw commando ontdekt!')
            else:
                honger += 1/drankhonger
        elif actie == 'bouwen' or actie == 'bo':
            bouwbaregebouwen = []
            if aantalhout >= 7 and aantalsteen >= 10 and aantalblad >= 12:
                bouwbaregebouwen.append('starter hut')
            if aantalhout >= 15 and aantalsteen >= 20:
                bouwbaregebouwen.append('stal')
                bouwbaregebouwen.append('bakkerij')
            if aantalhout >= 5:
                bouwbaregebouwen.append('boerderij')
            print(bouwbaregebouwen)
            gebouwd = input()
            if gebouwd in bouwbaregebouwen:
                if gebouwd == 'starter hut':
                    aantalhout -= 7
                    aantalsteen -= 10
                    aantalblad -= 12
                    starterhut = 1
                    commandos.append('koken')
                    print('Nieuw commando ontdekt!')
                elif gebouwd == 'stal':
                    aantalhout -= 15
                    aantalsteen -= 20
                    stal = 1
                elif gebouwd == 'boerderij':
                    aantalhout -= 5
                    boerderij = 1
                elif gebouwd == 'bakkerij':
                    aantalhout -= 15
                    aantalsteen -= 20
                    bakkerij == 1
                    commandos.append('bakken')
                    print('Nieuw commando ontdekt!')
            else:
                honger += 1/drankhonger
        elif actie == 'mijnwerken' or actie == 'mi' and stenenhouweel != 0:
            if ijzerenhouweel != 1:
                n = random.randint(0,4)
                if n == 0 or n == 1 or n == 2:
                    aantalsteen += (2*(n+1))
                    print("je hebt", 2*(n+1), "stenen gevonden")
                elif n == 3 or n == 4:
                    aantalijzer += 1
                    print("je hebt 1 ijzer gevonden")
            elif ijzerenhouweel == 1 and grotlevel >= 30:
                n = random.randint(1,15)
                if n >= 7:
                    aantalsteen += 5*(n+1)
                    print("Je hebt", 5*(n+1), "stenen gevonden.")
                elif n >= 9:
                    n = random.randint(1,5)
                    goud += n
                    print('Je hebt ', n, 'goud gevonden')
                elif n >= 11:
                    aantalijzer += 5
                    print("Je hebt 5 ijzer gevonden")
                elif n == 12:
                    print("Je hebt een diamant gevonden!")
                    aantaldiamant += 1
                else:
                    zombiehp = 15
                    print("Je bent een zombie tegengekomen!")
                    zombiedood = 0
                    if zombietegengekomen == 0:
                        print("Hier een kort hulptekstje over gevechten. Je kan alles wat een vijand doet aflezen op het scherm. Als hij aan het afwachten is, druk dan op A. Als hij aan het aanvallen is, druk dan op B.")
                    while zombiedood == 0:
                        aanval = random.randint(0,1)
                        if aanval == 0:
                            print("afwachten")
                            toetsingedrukt = input()
                            if toetsingedrukt == 'a':
                                hpverloren= random.randint(0,3)
                                print("hp verloren:", hpverloren, "schade gedaan:", nieuwedamage)
                                zombiehp -= nieuwedamage
                                hp -= hpverloren
                            else:
                                print("Je hebt de verkeerde toets ingedrukt")
                        else:
                            if toetsingedrukt == 'b':
                                print("Je hebt niets verloren en ook geen schade gedaan.")
                            else:
                                hpverloren = random.randint(1,3)
                                print("Je hebt de verkeerde toets ingedrukt en", hpverloren, "HP verloren.")
                        if zombiehp == 0:
                            print("Gefeliciteerd! Je hebt de zombie gedood!")
                            zombietegengekomen += 1
                            n = random.randint(1,25)
                            if n == 1:
                                print("Zombie heeft een zombiezwaard laten vallen!")
                                zombiezwaard = 1
            elif ijzerenhouweel == 1 and grotlevel >= 10:
                n = random.randint(1,10)
                if n >= 4:
                    print("Je hebt", 3*(n+1), "steen gevonden")
                    aantalsteen += 3*(n+1)
                elif n >= 6:
                    print("Je hebt 2 ijzer gevonden")
                    aantalijzer += 2
                elif n >= 8:
                    print('Je hebt', n/2, 'koper gevonden!')
                    aantalkoper += n/2
                elif n == 9:
                    zombiehp = 15
                    print("Je bent een zombie tegengekomen!")
                    zombiedood = 0
                    if zombietegengekomen == 0:
                        print("Hier een kort hulptekstje over gevechten. Je kan alles wat een vijand doet aflezen op het scherm. Als hij aan het afwachten is, druk dan op A. Als hij aan het aanvallen is, druk dan op B.")
                    while zombiedood == 0:
                        aanval = random.randint(0,1)
                        if aanval == 0:
                            print("afwachten")
                            toetsingedrukt = input()
                            if toetsingedrukt == 'a':
                                hpverloren= random.randint(0,3)
                                print("hp verloren:", hpverloren, "schade gedaan:", nieuwedamage)
                                zombiehp -= nieuwedamage
                                hp -= hpverloren
                            else:
                                print("Je hebt de verkeerde toets ingedrukt")
                        else:
                            if toetsingedrukt == 'b':
                                print("Je hebt niets verloren en ook geen schade gedaan.")
                            else:
                                hpverloren = random.randint(1,3)
                                print("Je hebt de verkeerde toets ingedrukt en", hpverloren, "HP verloren.")
                        if zombiehp == 0:
                            print("Gefeliciteerd! Je hebt de zombie gedood!")
                            zombietegengekomen += 1
                            n = random.randint(1,25)
                            if n == 1:
                                print("Zombie heeft een zombiezwaard laten vallen!")
                                zombiezwaard = 1
                elif n == 10:
                    n = random.randint(1,3)
                    print("Je bent in een gat in de grond gevallen en", n, "verdiepingen omlaag gevallen")
                    grotlevel += n
            krachtxp += 1
            grotlevel += 1
        elif actie == 'koken' or actie == 'k' and starterhut != 0:
            kookbareitems = []
            if aantalkleinvlees >= 1:
                kookbareitems.append('gekookt klein vlees')
            elif aantalgewoonvlees >= 1:
                kookbareitems.append('gekookt vlees')
            elif aantalgrootvlees >= 1:
                kookbareitems.append('gekookt groot vlees')
            print(kookbareitems)
            gekooktitem = input()
            if gekooktitem in kookbareitem:
                kookbareitems.remove(gekooktitem)
                if gekooktitem == 'gekookt klein vlees':
                    aantalkleinvlees -= 1
                    aantalgekooktkleinvlees += 1
                elif gekooktitem == 'gekookt vlees':
                    aantalgewoonvlees -= 1
                    aantalgekooktgewoonvlees += 1
                else:
                    aantalgrootvlees -= 1
                    aantalgekooktgrootvlees += 1
            else:
                honger += 1/drankhonger
        elif actie == 'bakken' or actie == 'ba' and bakkerij == 1:
            bakbareitems = []
            if aantalgraan >= 3:
                bakbareitems.append('brood')
            elif aantalgraan >= 3 and aantalfruit >= 2:
                bakbareitems.append('fruittaart')
            gebakken = input()
            if gebakken in bakbareitems:
                if gebakken == 'brood':
                    aantalgraan -= 3
                    aantalbrood += 1
                elif gebakken == 'fruittaart':
                    aantalgraan -= 3
                    aantalfruit -= 2
                    aantalfruittaart += 1
        elif actie == 'experimenteren' or actie == 'ex' and wetenschapstafel == 1:
            n = random.randint(0,2)
            if n == 0:
                ea.q()
            elif n == 1:
                eb.q()
            else:
                ec.q()
            wetenschapsxp += 1
        elif actie == 'vissen' or actie == 'vi' and vishengel == 1:
            n = random.randint(0,1)
            if n == 1:
                print('Je hebt een vis gevangen!')
                aantalvis += 1
            else:
                print('Je hebt wat afval gevangen. Je smeet het snel terug in het meer.')
            
        elif actie == 'eten' or actie == 'et':
            eetbaarvoedsel = []
            if aantalfruit >= 1:
                eetbaarvoedsel.append('fruit')
            if aantalkleinvlees >= 1:
                eetbaarvoedsel.append('klein vlees')
            if aantalgewoonvlees >= 1:
                eetbaarvoedsel.append('gewoon vlees')
            if aantalgrootvlees >= 1:
                eetbaarvoedsel.append('groot vlees')
            if aantalgekooktkleinvlees >= 1:
                eetbaarvoedsel.append('gekookt klein vlees')
            if aantalgekooktgewoonvlees >= 1:
                eetbaarvoedsel.append('gekookt vlees')
            if aantalgekooktgrootvlees >= 1:
                eetbaarvoedsel.append('gekookt groot vlees')
            if aantalbrood >= 1:
                eetbaarvoedsel.append('brood')
            if aantalfruittaart >= 1:
                eetbaarvoedsel.append('fruittaart')
            print("Je kan het volgende eten:", eetbaarvoedsel)
            gegetenvoedsel = input()
            if gegetenvoedsel in eetbaarvoedsel:
                eetbaarvoedsel.remove(gegetenvoedsel)
                if gegetenvoedsel == 'fruit':
                    aantalfruit -= 1
                    honger += 2
                    n == random.randint(0,9)
                    if n == 1:
                        print("Het fruit was rot! Hp verminderd met 4")
                        hp -= 4
                if gegetenvoedsel == 'klein vlees':
                    aantalkleinvlees -= 1
                    honger += 2
                if gegetenvoedsel == 'gewoon vlees':
                    aantalgewoonvlees -= 1
                    honger += 3
                if gegetenvoedsel == 'groot vlees':
                    aantalgrootvlees -= 1
                    honger += 4
                if gegetenvoedsel == 'gekookt klein vlees':
                    aantalgekooktkleinvlees -= 1
                    honger += 3
                if gegetenvoedsel == 'gekookt gewoon vlees':
                    aantalgekooktgewoonvlees -= 1
                    honger += 5
                if gegetenvoedsel == 'gekookt groot vlees':
                    aantalgekooktgrootvlees -= 1
                    honger += 7
                if gegetenvoedsel == 'brood':
                    aantalbrood -= 1
                    honger += 4
                if gegetenvoedsel == 'fruittaart':
                    aantalfruittaart -= 1
                    honger += 5
            elif gegetenvoedsel == '':
                honger += 1/drankhonger
            else:
                honger += 1/drankhonger
        elif actie == 'inventaris' or actie == 'i':
            print("Van welk voorwerp wil je het aantal weten?")
            inventarisvoorwerp = input()
            if inventarisvoorwerp == 'hout':
                print(aantalhout)
            elif inventarisvoorwerp == 'steen':
                print(aantalsteen)
            elif inventarisvoorwerp == 'vlees':
                print(aantalkleinvlees, aantalgewoonvlees, aantalgrootvlees, "Dat waren de rauwe vlezen geordend van klein naar groot. Nu volgen de gekooktevlezen:", aantalgekooktkleinvlees, aantalgekooktgewoonvlees, aantalgekooktgrootvlees)
            elif inventarisvoorwerp == 'blad' or inventarisvoorwerp == 'bladeren':
                print(aantalblad)
            elif inventarisvoorwerp == 'fruit':
                print(aantalfruit)
            elif inventarisvoorwerp == 'ijzer':
                print(aantalijzer)
            elif inventarisvoorwerp == 'brood':
                print(aantalbrood)
            elif inventarisvoorwerp == 'ivoor':
                print(aantalivoor)
            elif inventarisvoorwerp == 'diamant':
                print(aantaldiamant)
            elif inventarisvoorwerp == 'fruittaart':
                print(aantalfruittaart)
            elif inventarisvoorwerp == 'graan':
                print(aantalgraan)
            elif inventarisvoorwerp == 'geneeskrachtige kruiden':
                print(aantalgeneeskrachtigekruiden)
            elif inventarisvoorwerp == 'aluminium':
                print(aantalaluminium)
            elif inventarisvoorwerp == 'goud':
                print(goud)
            elif inventarisvoorwerp == 'koper':
                print(aantalkoper)
            else:
                print("Dit voorwerp stond niet in de inventaris.")
            honger += 1/drankhonger
        elif actie == 'recepten' or actie == 're':
            receptgevraagd = input('Welk recept wil je weten?')
            if receptgevraagd == 'starter hut':
                print('7 hout, 10 steen, en 12 bladeren')
            elif receptgevraagd == 'stenen houweel' or receptgevraagd == 'stenen zwaard' or receptgevraagd == 'stenen bijl':
                print('2 hout, 3 steen')
            elif receptgevraagd == 'ijzeren houweel' or receptgevraagd == 'ijzeren zwaard' or receptgevraagd == 'zeis' or receptgevraagd == 'ijzeren bijl':
                print('2 hout, 3 ijzer')
            elif receptgevraagd == 'gehoornde helm':
                print("4 hout, 5 ivoor")
            elif receptgevraagd == 'stal' or receptgevraagd == 'bakkerij':
                print("15 hout, 20 steen")
            elif receptgevraagd == 'boerderij':
                print("5 hout")
            elif receptgevraagd == 'aluminium':
                print('Om drie aluminium te maken heb je 2 koper en 1 goud nodig')
            elif receptgevraagd == 'geautomatiseerde oven':
                print('20 aluminium, 1 diamant, 5 koper, en 3 goud')
            elif receptgevraagd == 'geautomatiseerde boomgaard':
                print('3 diamant, 25 aluminium, 10 goud, en 10 koper')
            elif receptgevraagd == 'vishengel':
                print('3 hout, 2 bladeren')
            honger += 1/drankhonger
        elif actie == 'toverdrank drinken' or actie == 'td':
            drinkbaretoverdrank = []
            if krachtdrank >= 1:
                drinkbaretoverdrank.append('krachtdrank')
            if hpdrank >= 1:
                drinkbaretoverdrank.append('hpdrank')
            if hongerdrank >= 1:
                drinkbaretoverdrank.append('hongerdrank')
            gedronken = input()
            if gedronken in drinkbaretoverdrank:
                if gedronken == 'krachtdrank':
                    krachtdrank -= 1
                    effect = 1
                    drankkracht += 1
                if gedronken == 'hpdrank':
                    hpdrank -= 1
                    effect = 1
                    drankhp += 1
                if gedronken == 'hongerdrank':
                    hongerdrank -= 1
                    effect = 1
                    drankhonger += 1
            else:
                honger += 1/drankhonger
        elif actie == '':
            honger = 1
        else:
            honger += 1/drankhonger
            print("Ik heb het niet verstaan. Typ je het nog een keer?")
