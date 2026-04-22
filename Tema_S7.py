"""
Se cere de la tastatura o parola
Sa se verifice daca este puternica

Parola este considerata buna daca:
1. are cel putin 8 caractere
2. contine cel putin o cifra
3. contine cel putin o litera mare
4. contine cel putin o litera mica

Trebuie sa se afiseze "parola este puternica" sau ce conditii lipsesc

aditional
pentru a verifica daca un caracter este o cifra folosim functia .isdigit()
ex: if caracter.isdigit()

pentru a verifica daca un caracter este litera mare folosim functia .isupper()
ex: if caracter.isupper()

pentru a verifica daca un caracter este litera mica folosim functia .islower()
ex: if caracter.islower()
aveti nevoie de if si for
"""
# Rezolvare:
parola = input("Introdu parola: ")

are_cifra = False
are_litera_mare = False
are_litera_mica = False

for caracter in parola:
    if caracter.isdigit():
        are_cifra = True
    if caracter.isupper():
        are_litera_mare = True
    if caracter.islower():
        are_litera_mica = True

lipsuri = []

if len(parola) < 8:
    lipsuri.append("minim 8 caractere")
if not are_cifra:
    lipsuri.append("cel putin o cifra")
if not are_litera_mare:
    lipsuri.append("cel putin o litera mare")
if not are_litera_mica:
    lipsuri.append("cel putin o litera mica")

if len(lipsuri) == 0:
    print("Parola este puternica")
else:
    print("Parola nu este puternica. Lipsesc:")
    for conditie in lipsuri:
        print("-", conditie)

"""
Programul cere de la 5 utilizatori cate o nota pentu un produs, intre 1 si 5
Trebuie sa se afiseze:
1. cate note de 1, 2, 3, 4, 5 exista
2. media notelor
3. daca produsul este:
    - slab - daca media < 2.5
    - acceptabil - daca media este intre 2.5 si 4
    - excelent daca media > 4
reguli:
1. daca cineva introduce o nota invalida, trebuie ceruta din nou
2. foloseste while pentru validarea notei
3. for pentru cei 5 utilizatori
4. if pentru clasificare
"""
# Rezolvare:

numar_1 = 0
numar_2 = 0
numar_3 = 0
numar_4 = 0
numar_5 = 0

suma = 0

for i in range(1, 6):
    nota = int(input(f"Utilizatorul {i}, introdu o nota intre 1 si 5: "))

    while nota < 1 or nota > 5:
        nota = int(input("Nota invalida. Introdu din nou o nota intre 1 si 5: "))

    suma = suma + nota

    if nota == 1:
        numar_1 += 1
    elif nota == 2:
        numar_2 += 1
    elif nota == 3:
        numar_3 += 1
    elif nota == 4:
        numar_4 += 1
    elif nota == 5:
        numar_5 += 1

media = suma / 5

print("Numar note de 1:", numar_1)
print("Numar note de 2:", numar_2)
print("Numar note de 3:", numar_3)
print("Numar note de 4:", numar_4)
print("Numar note de 5:", numar_5)

print("Media notelor este:", media)

if media < 2.5:
    print("Produsul este slab")
elif media <= 4:
    print("Produsul este acceptabil")
else:
    print("Produsul este excelent")


"""
La intrarea intr-o parcare privata programul verifica mai multe masini
Pentru fiecare masina, se introduce:
1. Tipul vehiculului: auto, moto, camion
2. Daca are abonament: da / nu
3. Ora intrarii

Reguli:
1. camioanele nu ai voie dupa ora 18
2. motocicleta intra mereu
3. masinile fara anonament intra doar intre orele 08:00 si 20:00
4. pentru fiecare vehicul se afiseaza permis sau respins

foloseste for pentru mai multe vehicule
if pentru toate regulile
while pentru validare input
"""
# Rezolvare:

numar_vehicule = int(input("Cate vehicule verificam? "))

for i in range(1, numar_vehicule + 1):
    print(f"\nVehiculul {i}")

    tip = input("Introdu tipul vehiculului (auto/moto/camion): ").lower()
    while tip != "auto" and tip != "moto" and tip != "camion":
        tip = input("Tip invalid. Introdu auto, moto sau camion: ").lower()

    abonament = input("Are abonament? (da/nu): ").lower()
    while abonament != "da" and abonament != "nu":
        abonament = input("Valoare invalida. Introdu da sau nu: ").lower()

    ora = int(input("Introdu ora intrarii (0-23): "))
    while ora < 0 or ora > 23:
        ora = int(input("Ora invalida. Introdu o ora intre 0 si 23: "))

    if tip == "moto":
        print("Permis")
    elif tip == "camion":
        if ora > 18:
            print("Respins")
        else:
            print("Permis")
    elif tip == "auto":
        if abonament == "da":
            print("Permis")
        else:
            if ora >= 8 and ora <= 20:
                print("Permis")
            else:
                print("Respins")

