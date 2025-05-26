age = int(input("Bitte gib dein Alter ein: "))

if age < 18:
    print("Achtung ! Der Nutzer ist nicht volljährig.")
elif age == 18:
    print("Der Nutzer ist exakt 18 Jahre alt.")
else:
    print("Der Nutzer ist volljährig.")

print("Danke.")
