import pandas as pd




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