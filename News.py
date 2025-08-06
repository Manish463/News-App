import requests
import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("key")

url = "https://newsapi.org/v2/everything?language=en&q={}&from=2025-07-06&sortBy=popularity&apikey={}"

print("📰  Hello, friends! This is a News App. Get the latest news on your favorite topics. 📰\n")
print("1 : Technology")
print("2 : Health")
print("3 : Science")
print("4 : Sports")
print("5 : Weather")
print("6 : Others...")

opt = int(input("Enter your option: "))

if opt == 6:
    kind = input("Enter the keyword for news: ")

elif opt in [1, 2, 3, 4, 5]:
    l = ["technology", "health", "science", "sports", "weather"]
    if opt > 5 or opt < 0:
        raise Exception("Invalid option.")
    kind = l[opt-1]

else:
    print("Invalid option. Please try again.")

print("\nFetching news, please wait...\n" + "-"*80)
news = requests.get(url.format(kind, key)).json()

article = news["articles"]

print(f"\nTop 10 news of {kind}: \n")

for i in range(10):
    print(f"Title: {article[i]["title"]}".center(180))
    print(f"News description: {article[i]["description"]}")
    print(f"News: {article[i]["content"]}")
    print(f"To read full news follow this link: '{article[i]["url"]}'")
    print("-------------------------------------------------".center(180))
    print("\n")