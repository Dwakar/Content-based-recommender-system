import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
	return df[df.title == title]["index"].values[0] 
df = pd.read_csv("usercuisine1.csv")
profile = pd.read_csv('userprofile.csv')
df = pd.merge(df,profile)
features = ['budget','transport'] #pre cleaned datas
for feature in features:
	df[features] =  df[features].fillna('') #fill the Nan values with empty strings since in data keywords contins all Nan values
def combine_features(row): #takes entire row as input 
	try:
		return row['budget']+" "+ row['transport']
	except:
		print("Error:", row) #shows the eroor

df["combine_features"] = df.apply(combine_features, axis=1) #combines rows, axis used for pass data in rows 
print("Combined features",df["combine_features"].head())
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combine_features"])
cosine_sim = cosine_similarity(count_matrix)
cuisine_user_likes = "American"
cuisine_index = get_index_from_title(cuisine_user_likes) #gives index of the movie selected
similar_cuisine = list(enumerate(cosine_sim[cuisine_index])) #gives list of tuples with indexes
sorted_similar_cuisine = sorted(similar_cuisine,key= lambda x:x[1], reverse= True) #lambda for sorting second index of tuples
i=0
print("Top 5 similar cuisine to "+cuisine_user_likes+" are:\n")
for element in sorted_similar_cuisine:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break