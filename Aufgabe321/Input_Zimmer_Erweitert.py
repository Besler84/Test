def zimmer_einlesen():
    zimmer = {}
    zimmer["Zimmernummer"] = input("Zimmernummer: ")
    zimmer["Größe (m²)"] = input("Größe in m²: ")
    zimmer["Anzahl Fenster"] = input("Anzahl Fenster: ")
    zimmer["Stockwerk"] = input("Stockwerk: ")
    zimmer["Wandfarbe"] = input("Wandfarbe: ")
    zimmer["Bodenbelag"] = input("Bodenbelag: ")
    zimmer["Möbliert (Ja/Nein)"] = input("Möbliert (Ja/Nein): ")
    zimmer["Anzahl Steckdosen"] = input("Anzahl Steckdosen: ")
    zimmer["Tageslicht (Ja/Nein)"] = input("Tageslicht (Ja/Nein): ")
    zimmer["WLAN-Verfügbarkeit (Ja/Nein)"] = input("WLAN-Verfügbarkeit (Ja/Nein): ")
    return zimmer

def zimmer_ausgeben(zimmer):
    print("\n📋 Zimmerdaten:")
    for eigenschaft, wert in zimmer.items():
        print(f"{eigenschaft}: {wert}")

# Hauptprogramm
if __name__ == "__main__":
    datensatz = zimmer_einlesen()
    zimmer_ausgeben(datensatz)