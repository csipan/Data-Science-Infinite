import requests
from lxml import html

response = requests.get("http://www.nemzetisport.hu/labdarugo_nb_ii/gyasz-a-szegedi-futball-"
                        "elismert-jatekosat-edzojet-veszitette-el-2668799")

doc = html.fromstring(response.text)
paragraphs = doc.xpath("//div[contains(@class, 'cikkbody clearfix')]//p")

text_all = ''

for par in paragraphs:
  if par.text is not None and par.text is not "":
    text_all += str(par.text)

print(text_all)
