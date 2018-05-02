# grace.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from _spy.vitollino.main import STYLE
STYLE ["width"] = 900

homem_aranha = "https://http2.mlstatic.com/adesivo-decorativo-recortado-infantil-parede-homem-aranha-D_NQ_NP_14090-MLB4095351091_042013-F.jpg"
alice = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV0qG3TevJ2fNO4KblVuGlqxf1cH3kH-54QMEZ1QHwjmPLbNgy"
yoda = "http://obviousmag.org/renato_collyer/yoda2.jpg"
FLORESTA = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg"
pantano = "https://abrilmundoestranho.files.wordpress.com/2017/09/pantano-facebook.jpg?quality=70&strip=info"
final = "https://img.elo7.com.br/product/main/1790FA1/vela-ponto-de-interrogacao-vela-cerveja.jpg"

def tale():
    floresta = Cena(img=FLORESTA)
    floresta.vai()
    
tale()