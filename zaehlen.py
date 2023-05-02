def zaehlen_while(untergrenze, obergrenze): # Definiert Funktion
  count = untergrenze                       # Setzt count auf untergrenze
                                            # 
  while count <= obergrenze:                # Solange count kleiner gleich obergrenze
    print(count)                            # Ausgabe von count
    count += 1                              # count wird um 1 erhöht
                                            #
def zaehlen_for(untergrenze, obergrenze):   # Definiert Funktion
  for i in range(untergrenze, obergrenze):  # Wiederhole für i in range(untergrenze, obergrenze)
    print(i)                                # Ausgabe von i

untergrenze = int(input("Gib untergrenze ein: "))
obergrenze = int(input("Gib obergrenze ein: "))

zaehlen_while(untergrenze, obergrenze)
zaehlen_for(untergrenze, obergrenze)
