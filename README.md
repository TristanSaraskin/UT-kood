# Tehisintellekti objektituvastuse ning Dobot’i roboti rakendamine kabemängu mängimisel
Arvutinägemistehnoloogia alla kuuluvat objektituvastust rakendatakse 21. sajandil paljudes valdkondades, näiteks meditsiinis, turvatehnoloogias, isesõitvates autodes. Objektituvastust on võimalik rakendada olukordades, kus on vaja pildilt leida spetsiifilisi tunnuseid või objekte. Minimax’i algoritm on mänguteoorias rakendatav algoritm, mille eesmärgiks on vaheldumisi mängijate loogikat kasutades nullsummamängudes parima käigu leidmine.

Antud uurimistöö eesmärgiks oli koostada programm, mis suudab Haar kaskaadklassifitseerijal põhinevat objektituvastust, minimax’i algoritmi ning Dobot’i robotkätt kasutades mängida kabet. Eesmärgiga seonduvalt uuriti objektituvastuse tõhusust kabeseisu tuvastamisel ning minimax’i algoritmi tööle kuluva aja sõltuvust sügavusastmest.

Uurimistöös selgitati, kuidas töötab Haar kaskaadklassifitseerija, minimax’i algoritm ning milline on Dobot’i robotkäe liigutamiseks vajaminev kood. Objektituvastuse uurimiseks koostati Haar kaskaadklassifitseerijal põhinev kood, mida katsetati andmestiku peal, mis koosnes sajast kabeseisudest tehtud pildist. Minimax’i algoritmi uurimiseks koostati minimax’i algoritmil põhinev funktsioon, mida katsetati 64-ruudulise kabe algseisu peal.

Katsete käigus selgus, et objektituvastus tegi tuvastamisel keskmiselt 4,91 viga, mistõttu ei saa seda lugeda täpseks. Koodi tööd parandasid paremad valgustingimused ning kabelauast ja kabenditest eristuv taust. Minimax’i katsete tulemusena selgus, et algoritmi töötamisele kuluv aeg kasvas sügavusastme suurenedes eksponentsiaalselt.
