from bs4 import BeautifulSoup

file = open("website.html", mode='r')
content = file.read()

soup = BeautifulSoup(content, "html.parser")
# Get the title string from the HTML code
print(soup.title.string)

# Get all the anchor tags in the HTML
print(soup.find_all(name="a"))

# Get all the texts in the anchor tags
for tag in soup.find_all(name="a"):
    print(tag.get_text())

# Get the href in all the anchor tags
    print(tag.get("href"))

# Get hold of h1 using the id attribute name
print(soup.find(name="h1", id="name"))

# Get hold of h3 using the class attribute name
print(soup.find(name="h3", class_="heading"))

# Get hold of anchor tag using selectors
print(soup.select_one(selector="p a"))  # anchor tag that sits inside of paragraph tag

