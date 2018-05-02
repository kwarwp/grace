# grace.alexa.main.py

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900
spider = "http://pngimg.com/uploads/spider_man/spider_man_PNG89.png"
yoda = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1rPdnuQB1ZQc6mGizdqp2sveBpW3RpiLY5zo1lVVgySb7OrKaAA"
floresta = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIeUxwbjCdjWseCEvl6zrPev18NSEM-oUJXqGfajlKtjr2vQVi"
pantano = "https://vignette.wikia.nocookie.net/runescape2/images/3/3f/P%C3%A2ntano_de_Mort_Myre.png/revision/latest/scale-to-width-down/640?cb=20120331195051&path-prefix=pt"
final = "https://vignette.wikia.nocookie.net/runescape2/images/3/3f/P%C3%A2ntano_de_Mort_Myre.png/revision/latest/scale-to-width-down/640?cb=20120331195051&path-prefix=pt"

def historia():
 pantano = Cena(img=pantano)
 pantano.vai()
 
historia()