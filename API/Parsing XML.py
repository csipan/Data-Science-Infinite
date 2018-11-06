from bs4 import BeautifulSoup
import urllib.request
import requests
import lxml

source = urllib.request.urlopen("http://jira.greenfox.academy/secure/ViewProfile.jspa").read()

soup = BeautifulSoup(source, "html.parser")

# get the whole html format from the source
print(soup.prettify())

# get the first "title" (or others) with and without the title tag
print(soup.title)
print(soup.title.text)
print(soup.a.text)

# getting the info in a different way
# if we use the class form the html, we have to add an underscore like below
first_class = soup.find("fieldset", class_="parameters hidden")
print(first_class.prettify())

# getting deeper and deeper
div = soup.find("div", id="footer-logo")
print(div.a.text)

# using find all argument and iterating true the whole html
for ul in soup.find_all("ul", class_="atlassian-footer"):
    ul_text = ul.li
    print(ul_text.text)
    print("-----------------------------------------------------------")

# -------------------------------------------------------------------------------------------------------------------

source_2 = requests.get("http://jira.greenfox.academy/secure/ViewProfile.jspa").text

soup_2 = BeautifulSoup(source_2, "lxml")

print(soup_2.prettify())