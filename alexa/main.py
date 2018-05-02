# grace.alexa.main.py

from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"]= 900
SPIDER = "http://pngimg.com/uploads/spider_man/spider_man_PNG89.png"
ALICE = "https://banner.kisspng.com/20180203/iuw/kisspng-alices-adventures-in-wonderland-white-rabbit-queen-alice-in-wonderland-png-free-download-5a75c9682df831.6474162315176687121883.jpg"
YODA = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1rPdnuQB1ZQc6mGizdqp2sveBpW3RpiLY5zo1lVVgySb7OrKaAA"
FLORESTA = "https://img.elo7.com.br/product/zoom/12F2BAA/painel-de-festa-floresta-3-painel-em-tecido.jpg"
PANTANO = "https://vignette.wikia.nocookie.net/runescape2/images/3/3f/P%C3%A2ntano_de_Mort_Myre.png/revision/latest/scale-to-width-down/640?cb=20120331195051&path-prefix=pt"
FINAL = "https://vignette.wikia.nocookie.net/runescape2/images/3/3f/P%C3%A2ntano_de_Mort_Myre.png/revision/latest/scale-to-width-down/640?cb=20120331195051&path-prefix=pt"

def historia():
 floresta = Cena(img=FLORESTA)
 spider = Elemento(img = SPIDER, tit = "spider", style = dict(left = 100, top = 100, width = 100, hight = 100))
 spider_t = Texto(floresta, "Olha ela...")
 spider.vai = spider_t.vai
 spider.entra(floresta)
 floresta.vai()
 
historia()

