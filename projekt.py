import time
#print("Wpisz swoje składniki odzielone spacją: ")
lista_skladnikow_uzytkownika=["szynka","pomidor","kawior"]
#lista_skladnikow_uzytkownika=input().split()
lista_z_numerami_przepisow=[]

def porownywarka_skladnikow_uzytkownika_z_przepisem():

    
    file=open("skladniki.txt",'r')
    f=file.readlines()

    for line in f:
        ilosc_pasujacych_skladnikow=0
        skladniki_przepisu=line.split()
        ilosc=len(skladniki_przepisu)
        for x in lista_skladnikow_uzytkownika:
            if x in skladniki_przepisu:
                ilosc_pasujacych_skladnikow+=1

        if ilosc_pasujacych_skladnikow==ilosc-1:
            print(skladniki_przepisu)
            lista_z_numerami_przepisow.append(skladniki_przepisu[0]+"przepis")
        skladniki_przepisu.clear()
        
    file.close()
    return lista_z_numerami_przepisow

lista_z_numerami_przepisow= porownywarka_skladnikow_uzytkownika_z_przepisem()
print(lista_z_numerami_przepisow)




def odczytywanie_odpowiednich_przepisow(lista_z_numerami_przepisow):
    ktora_linia=0
    file=open("przepisy.txt",'r')
    lines=file.readlines()
    for line in lines:
        #ktora_linia+=1
        line=line.strip()
        if line in lista_z_numerami_przepisow: #dochodzi do lini z danym nr przepisu
            print(line)
            while line !='':
                line=file.readline()
                print(line)
            

    
    
        
                

odczytywanie_odpowiednich_przepisow(lista_z_numerami_przepisow)
