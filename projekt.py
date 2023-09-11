
#print("Wpisz swoje składniki odzielone spacją: ")
lista_skladnikow_uzytkownika=tuple()
lista_skladnikow_uzytkownika=input().split()

file=open("skladniki.txt","r")

f=file.readlines()

for line in f:
    skladniki_przepisu=tuple(line.split())

file.close()

print(skladniki_przepisu)
