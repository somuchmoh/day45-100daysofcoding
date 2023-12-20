from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_title = []
article_link = []
article_upvote = []
for tags in soup.find_all(name="a", rel="noreferrer"):
    article_title.append(tags.get_text())
    article_link.append(tags.get("href"))

for scores in soup.find_all(name="span", class_="score"):
    article_upvote.append(int(scores.get_text().split()[0]))

print(article_upvote)
print(article_title)
print(article_link)

largest_upvote = max(article_upvote)
index = article_upvote.index(largest_upvote)
print(article_link[index])
print(article_title[index])
