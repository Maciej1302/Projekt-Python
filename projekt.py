import pandas as pd
import csv


 
ing="salata pomidor ogorek chleb jajka bułka ser"

def szukarka(ing): 
    x=[]
    ing =ing.lower().split() 
    df = pd.read_csv('przepisy.csv')
    for index, row in df.iterrows():
        ingredients_list = row['ingredients'].lower().split() 
        if any(ingredient in ingredients_list for ingredient in ing) and all(ingredient in ing for ingredient in ingredients_list):
            x.append(row['description'])
    return x 

def check_user_existence(mail):
    df = pd.read_csv('users.csv')
    for index, row in df.iterrows():
        csv_mail=row['email']
        if mail == csv_mail:
            return True
    return False

def add_user(email,password,name,surname):
   data=[[email,password,name,surname]]
   file=open("users.csv","a",newline='')
   writer=csv.writer(file)

   writer.writerows(data)
   file.close()