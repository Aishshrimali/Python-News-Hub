import requests
import json

r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=aadac42660604333ada5650048cb42d0")

convert = r.json()
article = convert["articles"]
title = []
description=[]

for x in article:

    title.append(x["title"])
    #print(x["title"])
    
for y in article:

    description.append(y["description"])
    #print(y["description"])

for i in range(len(article)):
    #print(i)
    print(i,title[i])

def news():
    
    while True:
        choice=int(input("Enter title no to read news: "))
        
        for i in range(len(article)):
            
            if choice == i:
                
                print(i,description[i])
                print("\n")
                break
        else:
            print("not found")
                   
news()  