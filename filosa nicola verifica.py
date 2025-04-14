									#FILOSA NICOLA 4I 25/11/2024
totale_globale = 0

# Informiamo l'utente dell'offerta speciale all'inizio
print("Offerta speciale: Se scegli il Big MC, patatine e muffin, avrai diritto a un gadget gratuito!")

while True:
    totale = 0  # Reset totale per ogni nuovo ordine

    print("\nScegli un panino:\n")
    print("1. Big MC (€5.90)")
    print("2. Crispy MC Bacon (€4.80)")

    scelta = int(input("Inserisci il numero del panino che vuoi scegliere: "))

    if scelta == 1:
        totale += 5.90
        panino_scelto = "Big MC"
    elif scelta == 2:
        totale += 4.80
        panino_scelto = "Crispy MC Bacon"
    else:
        print("Scelta non valida. Riprova.")
        continue  # Riprova il ciclo se la scelta è invalida

    print("\nScegli il secondo che desideri:\n")
    print("1. patatine (€3.00)")
    print("2. Nuggets (€2.80)")
    print("3. Alette di pollo (€3.10)")

    scelta = int(input("Inserisci il numero della bibita che vuoi scegliere: "))

    if scelta == 1:
        totale += 2.70
        bibita_scelta = "patatine"
    elif scelta == 2:
        totale += 2.80
        bibita_scelta = "Nuggets"
    elif scelta == 3:
        totale += 3.10
        bibita_scelta = "Alette di pollo"
    else:
        print("Scelta non valida. Riprova.")
        continue  # Riprova il ciclo se la scelta è invalida

    print("\nScegli il dessert che desideri:\n")
    print("1. muffin (€1.00)")
    print("2. McFlurry (€3.80)")
    print("3. milkshake (€4.10)")

    scelta = int(input("Inserisci il numero del dessert che vuoi ordinare: "))

    if scelta == 1:
        totale += 1.00
        dessert_scelto = "muffin"
    elif scelta == 2:
        totale += 3.80
        dessert_scelto = "McFlurry"
    elif scelta == 3:
        totale += 4.10
        dessert_scelto = "milkshake"
    else:
        print("Scelta non valida. Riprova.")
        continue  # Riprova il ciclo se la scelta è invalida

    print("\nScegli il metodo di pagamento:")
    print("1. Carta")
    print("2. Contanti")

    metodo = int(input("Inserisci il numero del metodo di pagamento: "))

    if metodo == 1:
        print("Hai scelto di pagare con carta.")
    elif metodo == 2:
        print("Hai scelto di pagare in contanti.")
    else:
        print("Scelta non valida. Riprova.")
        continue  # Riprova il ciclo se la scelta è invalida

    print("\nScegli se è da asporto o al tavolo:")
    print("1. Da asporto")
    print("2. Al tavolo")

    opzione = int(input("Inserisci il numero della scelta: "))

    if opzione == 1:
        print("Hai scelto da asporto.")
    elif opzione == 2:
        tavolo = input("Inserisci il numero del tavolo: ")
        print(f"Hai scelto al tavolo, numero del tavolo: {tavolo}.")
    else:
        print("Scelta non valida. Riprova.")
        continue  # Riprova il ciclo se la scelta è invalida

    caffe = input("Vuoi un caffè? (sì/no): ")
    if caffe == "sì":
        totale += 1.00

    totale_globale += totale
    print("Totale ordine corrente = €{:10.2f}".format(totale))

    # Verifica se l'utente ha diritto al gadget
    if panino_scelto == "Big MC" and bibita_scelta == "patatine" and dessert_scelto == "muffin":
        print("Hai diritto al gadget che potrai ritirare gratuitamente!")

    continua = input("Vuoi fare un altro ordine? (sì/no): ")
    if continua != "sì":
        print("Totale finale = €{:10.2f}".format(totale_globale))
        print("Grazie per il tuo ordine!")
        break