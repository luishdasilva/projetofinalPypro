from requests import get
from bs4 import BeautifulSoup



navegar = get("https://pt.wikipedia.org/wiki/Sociologia_das_hist%C3%B3rias_em_quadrinhos")
tags = BeautifulSoup(navegar.text, "html5lib")
tds = tags.find_all("a", attrs={"class" : "mw-redirect" })
td = [a.text for a in tds]
refe = ["https://pt.wikipedia.org/wiki/Filmes_do_Universo_Cinematogr%C3%A1fico_Marvel" + h2["href"] for h2 in tds ]
refe
