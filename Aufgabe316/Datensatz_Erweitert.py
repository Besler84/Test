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

# Ausgabe in einem Satz

sentence = (
    f"{name} ist ein {age}-jähriger, {trait}er {gender} mit {hair_color}en Haaren "
    f"und {eye_color}en Augen. Er ist {height} groß, wiegt {weight}, "
    f"arbeitet als {job} und hat als Hobby das {hobby}."
)

print(sentence)