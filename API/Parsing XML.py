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

source_2 = requests.get("http://www.nemzetisport.hu/bajnokok_ligaja/"
                        "bl-gond-a-repteren-kesve-erkezett-a-dortmund-madridba-2667603").text

soup_2 = BeautifulSoup(source_2, "lxml")

article = soup_2.find("article")
headline = article.h1.text
news_summary = article.p.text
news_text_1 = article.find("div", class_="cikkbody clearfix")

print(headline)
print(news_summary)

for news in news_text_1.find_all("p"):
    if news.text[0] != " ":
        print(news.text)


