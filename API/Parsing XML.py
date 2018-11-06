from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen("http://www.nemzetisport.hu/magyar_valogatott/marco-rossi-sohasem-volt-bajom-dzsudzsak-balazssal-2667547").read()

# miért nem megy az idézőjelben az lxml
soup = BeautifulSoup(source, "html.parser")

print(soup.h1)
