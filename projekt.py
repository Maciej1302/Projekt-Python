import pandas as pd

 
df = pd.read_csv('przepisy.csv')
 
ing = "salata pomidor ogorek chleb jajka bułka ser"
ing =ing.lower().split() 
 
for index, row in df.iterrows():
    ingredients_list = row['ingredients'].lower().split() 
    if any(ingredient in ingredients_list for ingredient in ing) and all(ingredient in ing for ingredient in ingredients_list):
        print(row['description'])