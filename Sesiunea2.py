# print("salut") #pasul 1
# print("Astazi invatam python") #pastul 2
# print("Aceasta este prima lectie") #pasul 3
# print(10)
# print(3.14)
# print(2+3)
# print(10-4)
# print(5*2)
#
#
# nume = "Ana"
# print(nume)
#
#
# varsta = 25
# print(varsta)
#
#
# print(type(nume))
# print(type(varsta))
#
#
# print(nume, varsta) #Python pune automat spatiu intre ele cand sunt separate prin virgula
# print("Numele meu este:", nume)


#mai multe moduri de afisare cu print()

# #1. cu virgula in print()
nume = "Ana"
#print(nume)
varsta = 25
print("Numele este", nume)
print("varsta este:", varsta)
#
# #2. cu plus intre stringuri
prenume = "Ion"
nume_familie = "Popescu"
# print(prenume + " " + nume_familie) #cu plus ambele parti trebuie sa fie stringuri
#print("Am" + varsta + "ani") #eroare pt ca varsta e nr intreg, nu string
print("Am " + str(varsta) + " ani") #varianta corectata, convertim nr intreg in string

#3. cu f-string/cu acolade
nume="Andrei"
varsta=21
print(f"Numele meu este {nume} si am {varsta} ani") #litera f inainte de string ne spune ca in interior vom pune variabile, iar aici variabilele se scriu intre acolade

#4. cu metoda format()
nume="Elena"
varsta=20
print("Ma numesc {} si am {} ani".format(nume, varsta)) #sa fiu atenta la ordinea logica a variabilelor ca sa aiba propozitia sens

print(len(nume)) #numara cate caractere are textul



#1. str - string - text
nume="Ana"
oras="Cluj"
mesaj = "Salut"

#ambele variante de scriere sunt corecte:
a = "Python"
b = 'curs'
x="10" # text nu nr

#Triple quotes - pt string cu mai multe randuri
text =f"""rand 1 {a}
rand 2
rand 3"""
#poate fi folosit si pt comentariu pe mai multe randuri
print(text)
#diferenta dintre " " si """ """: " " scriem de obicei texte pe o singura linie, iar cu cele triple putem scrie texte pe mai multe linii/texte mai lungi
#mai putem scrie pe linii si asa:
print("rand 1\nrand 2\nrand 3")

#int - integer - nr intreg

#float - nr zecimale
inaltime = 1.75
pret = 19.99
#in python zecimalele se scriu cu punct nu cu virgula
print(15.5)
print(15,5+2)

#bool - boolean - true/false
ok=True
nok=False
print (ok, nok)


variabila = None #variabila goala
