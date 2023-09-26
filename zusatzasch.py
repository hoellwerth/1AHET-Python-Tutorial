import random                 #Importiere das Tool "random", welches ich brauche um später eine zufällige Zahl zu generieren.




def kontostand(geld):                   #Ich erstelle eine Funktion namens "kontostand", welche ich immer aufrufen kann, wenn ich will, dass der aktuelle Kontostand gezeigt wird

    print("Aktueller Kontostand:", geld)   #zeigt den aktuellen Kontostand an




def ende(geld):                          # Ich erstelle eine Funktion namens "ende", die ich aufrufe, wenn das man sich dafür entscheidet nicht mehr weiterzuspielen.

    print("Schade, dass Sie nicht mehr spielen wollen. Ihr Kontostand beträgt:", geld) #Es wird ein Text ausgegeben und zeigt nochmal den Kontostand an, mit dem man das Spiel verlässt.




geld = int(input("Mit wie viel Geld wollen Sie spielen? ")) #Der Spieler wird gefragt mit wie viel Geld er spielen will, bevor das Spiel beginnt. Die Eingabe wird unter der Variable "geld" gespeichert.

kontostand(geld) #Ruft die Funktion namens "kontostand" auf, damit der aktuelle Kontostand angezeigt wird.




while True: #Ich packe den restlichen Code in eine Schleife, die nur endet wenn die Funktion "ende" (außerhalb der Schleife) aufgerufen wird.

    geldsetzen = int(input("Wie viel Geld wollen Sie auf diese Runde setzen? Wenn Sie richtig raten, bekommen Sie das zehnfache! Wenn Sie falsch liegen, verlieren Sie das Geld! Wenn Sie nicht mehr spielen wollen, geben Sie eine negative Zahl ein! ")) #Man startet nun eine Runde und man wird gefragt, wie viel man auf die Runde setzen möchte. Die Eingabe wird unter "geldsetzen" gespeichert.




    if geldsetzen < 0: #Wenn man eine negative Zahl eingegeben hat, will man nicht mehr spielen

        ende(geld)   #Die Funktion "ende" wird aufgerufen

       




    anzahlwuerfe = int(input("Wie oft soll gewürfelt werden? ")) #Man wird gefragt wie oft man würfeln will. Der eingegebene Wert wird unter "anzahlwuerfe" gespeichert

    paschguess = int(input("Wie oft wird ein Pasch gewürfelt? ")) #Nun kann man raten, wie oft ein Pasch gewürfelt wird. Der eingegebene Wert wird unter "paschguess" gespeichert




    def pasch(anzahlwuerfe): #Erstelle eine Funktion namens "pasch"

        paschanzahl = 0 #Der Variablenwert wird auf null gesetzt, bevor er verwendet wird

        for _ in range(anzahlwuerfe): #Ich erstelle eine Schleife die so oft läuft, wie man zuerst eingegeben hat.

            wurf1 = random.randint(1, 6) #Die erste zufällige Zahl wird erstellt und unter "wurf1" gespeichert

            wurf2 = random.randint(1, 6) #Die zweite zufällige Zahl wird erstellt und unter "wurf2" gespeichert

            print(wurf1) #Die erste Zahl wird ausgegeben

            print(wurf2) #Die zweite Zahl wird auch ausgegeben

            if wurf1 == wurf2: #Wenn die Zahlen den gleichen Wert haben, werden die nächsten Befehle ausgeführt

                print(" - Pasch") #Es wird Pasch ausgegeben

                paschanzahl += 1 #Erhöht den Wert der Variable "paschanzahl" um 1

        return paschanzahl #Die Funktion schickt den Wert der Variable "paschanzahl" zurück dahin, wo sie aufgerufen wurde




    paschanzahl = pasch(anzahlwuerfe) #Die Funktion "pasch" wird aufgerufen und der zurückkommende Wert wird unter paschanzahl gespeichert




    if paschguess == paschanzahl: #Wenn man nun richtig geraten hat, werden die nächsten Befehle ausgeführt

        print("Glückwunsch! Sie haben richtig erraten, wie oft Pasch gewürfelt wurde.") #Es wird ein Text ausgegeben

        geld += geldsetzen * 10 #Der Variablenwert von "geld" wird um das zehnfache vom gesetzten Geld (Variablenwert von "geldsetzen") erhöht

    else: #Wenn man nicht richtig geraten hat, werden die nächsten Befehle ausgeführt

        if paschanzahl > paschguess: #Wenn man zu wenig oft geraten, werden die nächsten Befehle ausgeführt

            print("Es wurde öfter Pasch gewürfelt als Sie geraten haben.") #Es wird ein Text ausgegeben

            geld -= geldsetzen #Der Variablenwert von "geld" wird um das gesetzte Geld (Variablenwert von "geldsetzen") subtrahiert

        else: #Wenn man zu oft geraten, werden die nächsten Befehle ausgeführt

            print("Es wurde weniger oft Pasch gewürfelt als Sie geraten haben.") #Es wird ein Text ausgegeben

            geld -= geldsetzen #Der Variablenwert von "geld" wird um das gesetzte Geld (Variablenwert von "geldsetzen") subtrahiert




    kontostand(geld) #Die Funktion "kontostand" wird aufgerufen



