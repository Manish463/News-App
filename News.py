import requests
from My_key import key

url = "https://newsapi.org/v2/everything?language=en&q={}&from=2025-05-24&to=2025-05-23&sortBy=popularity&apiKey={}"

print("Hello, friends this is a news app using this you can get some kind of news.")
print("1 : Technology")
print("2 : Health")
print("3 : Science")
print("4 : Sports")
print("5 : Weather")

l = ["technology", "health", "science", "sports", "weather"]
ind = int(input("enter your option: "))

if ind>5 or ind<0:
    raise Exception("Invalid option.")
kind = l[ind-1]

news = requests.get(url.format(kind, key)).json()
article = news["articles"]

print(f"\nTop 3 news of {kind}: \n")

for i in range(3):
    print(f"Title: {article[i]["title"]}".center(180))
    print(f"News description: {article[i]["description"]}")
    print(f"News: {article[i]["content"]}")
    print(f"To read full news follow this link: '{article[i]["url"]}'")
    print("-------------------------------------------------".center(180))
    print("\n")