import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
movie_list = response.text

soup = BeautifulSoup(movie_list, "html.parser")
movie_titles = []
for tags in soup.find_all(name="h3", class_="title"):
    movie_titles.append(tags.get_text())

with open ("movies.txt", mode='w') as file:
    for i in range(1, 101):
        file.write(f"{movie_titles[-i]} \n")


