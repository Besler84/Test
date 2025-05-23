print('Datensatz und Satzbau')
print('')

# Personendaten

name = "Max Mustermann"
age = 30
gender = "Mann"
height = "1,80m"
weight = "75kg"
eye_color = "braun"
hair_color = "schwarz"
job = "Softwareentwickler"
hobby = "Lesen"
trait = "freundlich"

# Satzbau

output_sentense = name + " ist ein " +  str(age) + "-jähriger, " + trait + "er " + gender + " mit " + hair_color + "en Haaren und " +  eye_color + "en Augen. Er ist " + height + " groß, wiegt " + weight + ", arbeitet als " + job + " und hat als Hobby das " + hobby + "."

# Ausgabe des Satzes

print(output_sentense)