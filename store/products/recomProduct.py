from productApi import get_products
import os
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity



products= get_products()



products_csv=[]
for i in range (len(products)):
    product = {"name":products[i] , "index":i}
    products_csv.append(product)


if not os.path.exists("data"):
    os.makedirs("data")



#Write the course descriptions to a CSV file in the data directory
with open("data/products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "index"])
    writer.writeheader()
    for product in products_csv:
        writer.writerow(product)


df = pd.read_csv("data/products.csv")



# ignore unneccessary words like this , is , ...
tfidf = TfidfVectorizer(stop_words="english")
# fill null with blank
df["name"] = df['name'].fillna("")

#develop our vector model based on this column
tfidf_matrix = tfidf.fit_transform(df['name'])

#build cosin similarity , it takes the matrix of the descriptions and create a reference of each movie with the other
cosine_sim = cosine_similarity(tfidf_matrix , tfidf_matrix)

#for each title assign an index
#indices = pd.Series(df.index , index=df['title']).drop_duplicates()




def get_recommendations(tag, cosine_sim=cosine_sim, df=df):
    results=[]
    rows = df.shape[0]
    for item in tag :
        if(item not in df['name'].values):
            list_row = [item, rows]
            df.loc[len(df)] = list_row
            
            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(df['name'])


            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


        
        idx = df[df['name'] == item].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        sim_scores = sim_scores[0:3]
        product_indices = [i[0] for i in sim_scores]
        
        #results.append(list(df['title'].iloc[course_indices]))
        for index in product_indices:
            name = df['name'].iloc[index]
            if name != "new product" and name not in results:
                results.append(name)
    return results


print(get_recommendations(['palestine']))