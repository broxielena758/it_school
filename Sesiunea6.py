#Exercitiul1:
# sa se calculeze suma tuturor nr pare de la 1 la 20 (inclusiv)

suma = 0
for i in range(1,21):
    if i%2==0:
        suma += i
print (suma)

#Exercitiul2:
# sa se parcurga numerele de la 1 la 30 inclusiv si sa se afiseze cate numere sunt: mai mari decat 10 si pare

k=0
for i in range(1,31):
    if i>10 and i%2==0:
        k+=1
print(k)

#Exercitiul3:
# sa se calculeze suma numerelor de la 1 la 100 care sunt dizibile si cu 3 si cu 5

s=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        s += i
print(s)

#Exercitiul4:
# sa se parcurga nr de la 1 la 10. pt fiecare nr. se calc: rezultat = i*3-2. sa se afle cea mai mare valoare obtinuta

max=0
for i in range(1, 11):
    rezultat = i*3-2
    if rezultat>max:
        max=rezultat
print(max)

#Exercitiul5:
# se da un text. pt. fiecare vocala incrementam cu 2 puncte, iar pt fiecare consoana cu 1 punct. la final afiseaza total puncte

text = "python"
puncte = 0
for litera in text:
    if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u":
        puncte+=2
    else:
        puncte+=1
print(puncte)